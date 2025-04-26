from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    user_id: str
    query: str

class ChatResponse(BaseModel):
    response: str
    sources: List[str]
