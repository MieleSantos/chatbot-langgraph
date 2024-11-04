import streamlit as st

# from groq import Groq
# from config_env import set_env
from assistent import stream_graph_updates

# set_env()
# client = Groq()
# client = Groq()
# completion = client.chat.completions.create(
#     model='llama3-groq-70b-8192-tool-use-preview',
#     messages=[],
#     temperature=0.5,
#     max_tokens=1024,
#     top_p=0.65,
#     stream=True,
#     stop=None,
# )
with st.sidebar:
    st.header('Descrição')

    st.write("""Desafio Tecnico - chatbot interativo que não apenas responda perguntas,
             mas também aprenda e se adapte com base nas interações do usuário.
  """)


st.title('💬 Chatbot')

if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {'role': 'assistant', 'content': 'Como posso ajudar?'}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

if prompt := st.chat_input():
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    st.chat_message('user').write(prompt)
    stream_graph_updates(prompt, st)
    # response = client.chat.completions.create(
    #     model='llama3-groq-70b-8192-tool-use-preview',
    #     messages=st.session_state.messages,
    # )
