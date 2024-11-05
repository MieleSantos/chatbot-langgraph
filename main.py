import streamlit as st

from assistent import Agent

with st.sidebar:
    st.header('Descrição')

    st.write("""Desafio Tecnico - chatbot interativo que não apenas responda perguntas,
             mas também aprenda e se adapte coms base nas interações do usuário.
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

    agent = Agent(st=st)
    agent.stream_graph_update(prompt)
