import os

from dotenv import load_dotenv


def set_env():
    """
    Função para seta a API_KEY na variásvel de ambiente
    Raises:
        ValueError: Error caso não encontre a API_KEY
    """
    # carregando a variável que esta no .env
    load_dotenv()

    if not os.getenv('API_KEY'):
        raise ValueError('Api key não encontrada')

    os.environ['GROQ_API_KEY'] = os.getenv('API_KEY')
