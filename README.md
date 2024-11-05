
## Desafio - Python_Aprendizado Contínuo

Desenvolver um chatbot interativo que não apenas responda perguntas, mas também
aprenda e se adapte com base nas interações do usuário.<br> O chatbot deve armazenar
informações relevantes sobre um tema específico apenas quando o usuário enviar algo
verdadeiro (não deve aceitar correções falsas)<br> ou quando se trata de preferências por
exemplo, preferir um tom mais formal).

### Requisitos
- **UI:** Você deve criar uma interface visual do chatbot (usando streamlit ou qualquer
outra ferramenta para a construção rápida da ui, ela não é a prioridade do teste)
- **LangGraph e Langchain:** Devem ser usados para a construção da solução
- **LLM:** Qualquer um de sua preferência, contanto que, haja uma variável de ambiente
para colocarmos nossa chave de api (dica: usar os llms da Groq é grátis)
- **Base de dados vetorial:** Para armazenar as informações relevantes, pode ser
qualquer uma, contanto que estejam em um container docker no projeto.

### Entrega:
- **Código no GitHub:** O código-fonte do projeto deve ser disponibilizado em um
repositório público no GitHub.
- **Documentação:** Uma documentação detalhada que explique como instalar as
dependências e executar a aplicação localmente, incluindo exemplos de uso e
configurações necessárias.
- **Container Docker:** O projeto deve incluir um Dockerfile que permita criar uma
imagem Docker, facilitando a execução da aplicação em diferentes ambientes sem
conflitos de dependência.

### Observações

Este desafio será discutido durante a entrevista, proporcionando a oportunidade de você
apresentar suas soluções e decisões tomadas durante o desenvolvimento.<br> Além disso, é
uma excelente chance para enriquecer seu portfólio.<br> Se você já possui um projeto que
utiliza as tecnologias mencionadas, sinta-se à vontade para compartilhá-lo conosco, o que
tornará a implementação deste desafio desnecessária.<br>
Sua habilidade em refinar as respostas do modelo de lingua


## Tecnologias Utilizadas

- **Python**: Linguagem principal para lógica do agente e cálculos.
- **Poetry**: Para gerenciar as dependencias do projeto
- **streamilt**: Para construir a interface do chatbot
- **LangChain**: Framework para desenvolver aplicativos que utilizam modelos de linguagem.
- **LangGraph**: Framework para na elaboração de worflows entre Agents e ferramentas, permitindo a criação de uma memória de estado a cada interação e a relação entre os itens presentes nesse tipo de fluxo, baseado em grafos.
- **Groq API**: Utilizado para interpretar as consultas em linguagem natural e gerar respostas.
- **Docker**: Para criar imagem do projeto

## Estrutura do projeto
- **main.py**: script principal responsável pela interface **[streamilt](https://streamlit.io/)**
- **config_env.py**: script para seta a variavel de ambiente com a API_KEY
- **assistent.py**:  script com a logica do chatbot
- **docker-compose.yml/Dockerfile**: Para criação do container da aplicação


## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/MieleSantos/chatbot-langgraph.git
    ```

2. Na raiz do projeto, criei um arquivo **.env**  com a chave **API_kEY** da **GROQ**:
    ```
    API_KEY=<sua_api_key>
    ```
3. Com o **docker** instalado, no diretorio do projeto, execute:
   ```bash
   docker-compose up --build -d
   ```


### Execução do Chatbot

Com o container rodando, acesse o navegador **http://localhost:8501/** e interaja com o chatbot




## checkin
- interface- ok
- docker - ok
- langchain - ok
- llm- ok
- LangGraph - implementando
- Base de dados vetorial - implementando
- Documentação: - implementando