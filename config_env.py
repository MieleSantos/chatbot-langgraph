import os

from dotenv import load_dotenv


def set_env():
    load_dotenv()
    if not os.getenv('API_KEY'):
        raise ValueError('Api key não encontrada')
    os.environ['GROQ_API_KEY'] = os.getenv('API_KEY')
