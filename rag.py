import os
import openai
import numpy as np

try:
    import pinecone
    PINECONE_ENABLED = True
except ImportError:
    PINECONE_ENABLED = False

import faiss
from app.config import settings

class RAGEngine:
    def __init__(self):
        openai.api_key = settings.openai_api_key
        if PINECONE_ENABLED and all([settings.pinecone_api_key, settings.pinecone_env, settings.pinecone_index]):
            pinecone.init(api_key=settings.pinecone_api_key, environment=settings.pinecone_env)
            self.index = pinecone.Index(settings.pinecone_index)
            self.backend = 'pinecone'
        else:
            self.index = faiss.read_index(settings.vector_db_path)
            self.backend = 'faiss'

    def retrieve(self, query: str, k: int = 5):
        q_vec = self._embed_text(query)
        if self.backend == 'pinecone':
            res = self.index.query([q_vec.tolist()], top_k=k, include_metadata=True)
            chunks = [match['metadata']['text'] for match in res['matches']]
            sources = [match['metadata'].get('source', '') for match in res['matches']]
        else:
            D, I = self.index.search(np.array([q_vec]), k)
            chunks = ["Chunk text ..."]  # placeholder
            sources = ["Source A"]
        return chunks, sources

    def generate(self, prompt: str) -> str:
        resp = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}]
        )
        return resp.choices[0].message.content

    def _embed_text(self, text: str) -> np.ndarray:
        embedding = openai.Embedding.create(input=text, model="text-embedding-ada-002")
        return np.array(embedding.data[0].embedding, dtype=np.float32)
