from typing import Annotated

from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

from config_env import set_env

set_env()


# estrutura do estado do chatbot
class State(TypedDict):
    messages: Annotated[list, add_messages]


class Agent:
    def __init__(self, st):
        self.model = ChatGroq(model='llama-3.2-11b-text-preview', temperature=0.5)
        self.st = st
        self.prompt_template = self._create_prompt_template()
        self.memory = MemorySaver()
        self.graph_builder = StateGraph(State)
        # adicionar o nó chatbot ao grafo,
        self.graph_builder.add_node('chatbot', self.chatbot)
        # cria uma conexão que indica que a execuão do grafo começa no chatbot
        self.graph_builder.add_edge(START, 'chatbot')
        # apos o chatbot processar a entrada do usuario o grafo deve encerrar a execução
        self.graph_builder.add_edge('chatbot', END)

        # compila o grafo de estados configurado,tornando-o pronto para ser usado
        self.graph = self.graph_builder.compile(checkpointer=self.memory)
        self.config = {'configurable': {'thread_id': '1'}}

    # definindo catbot que aceita um estado e retonra uma nova mensagem
    # invocando o modelo
    def _create_prompt_template(self):  # noqa: PLR6301
        prompt = """
        Responsa as interacões do usuário com informações validas.
        usando um tom mais formal.
        Pergunta: {q}
        """
        return PromptTemplate.from_template(prompt)

    def chatbot(self, state: State):
        messages = state['messages']
        input_question = self.prompt_template.format(q=messages)
        return {'messages': [self.model.invoke(input_question)]}

    def stream_graph_update(self, user_input):
        # processa a entrada do usuaário, criando uma mensagem e passando pelo grafo
        for event in self.graph.stream(
            {'messages': [('user', user_input)]}, self.config
        ):
            # itera sobre os eventos gerados pelo evento,
            # exibe a  ultima mensagem da resposta do assistente
            for value in event.values():
                msg = value['messages'][-1].content
                # print('Assistant:', value['messages'][-1].content)
                print('Assistant:', msg)
                # msg = response.choices[0].message.content

                self.st.session_state.messages.append({
                    'role': 'assistant',
                    'content': msg,
                })

                self.st.chat_message('assistant').write(msg)
