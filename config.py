import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    openai_api_key: str = os.getenv("OPENAI_API_KEY")
    vector_db_path: str = os.getenv("VECTOR_DB_PATH")
    pinecone_api_key: str = os.getenv("PINECONE_API_KEY")
    pinecone_env: str = os.getenv("PINECONE_ENV")
    pinecone_index: str = os.getenv("PINECONE_INDEX")

settings = Settings()
