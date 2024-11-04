from typing import Annotated

from langchain_groq import ChatGroq
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

from config_env import set_env

set_env()


# estrutura do estado do chatbot
class State(TypedDict):
    messages: Annotated[list, add_messages]


# inicializando o construtor do grafo de estado
graph_builder = StateGraph(State)

model = ChatGroq(model='llama-3.2-11b-text-preview', temperature=0.5)


# definindo catbot que aceita um estado e retonra uma nova mensagem invocando o modelo
def chatbot(state: State):
    return {'messages': [model.invoke(state['messages'])]}


# adicionar o nó chatbot ao grafo,
graph_builder.add_node('chatbot', chatbot)

# cria uma conexão que indica que a execuão do grafo começa no chatbot
graph_builder.add_edge(START, 'chatbot')


graph_builder.add_edge('chatbot', END)
# apos o chatbot processar a entrada do usuario o grafo deve encerrar a execução

# compila o grafo de estados configurado,tornando-o pronto para ser usado
graph = graph_builder.compile()


def stream_graph_updates(user_input: str, st):
    # processa a entrada do usuaário, criando uma mensagem e passando pelo grafo
    for event in graph.stream({'messages': [('user', user_input)]}):
        # itera sobre os eventos gerados pelo evento,
        # exibe a  ultima mensagem da resposta do assistente
        for value in event.values():
            msg = value['messages'][-1].content
            # print('Assistant:', value['messages'][-1].content)
            print('Assistant:', msg)
            # msg = response.choices[0].message.content

            st.session_state.messages.append({'role': 'assistant', 'content': msg})

            st.chat_message('assistant').write(msg)
