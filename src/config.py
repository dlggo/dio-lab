import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY não encontrada. "
        "Crie um arquivo .env na raiz do projeto."
    )

if not OPENAI_MODEL:
    raise ValueError(
        "OPENAI_MODEL não encontrada no arquivo .env."
    )