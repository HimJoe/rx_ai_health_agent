from fastapi import FastAPI, HTTPException
from app.schemas import ChatRequest, ChatResponse
from app.profile_manager import ProfileManager
from app.rag import RAGEngine
from app.safety import SafetyModule

app = FastAPI()
rag = RAGEngine()

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # Emergency check
    if SafetyModule.check_emergency(request.query):
        return ChatResponse(
            response="This may be an emergency. Please seek immediate medical attention!",
            sources=[]
        )

    profile = ProfileManager.get_profile(request.user_id)
    chunks, sources = rag.retrieve(request.query)
    # Build prompt
    prompt = f"User Profile: {profile}\n" + \
             f"Query: {request.query}\n" + \
             "Knowledge:\n" + "\n".join(chunks)
    answer = rag.generate(prompt)
    answer = SafetyModule.disclaimer(answer)
    return ChatResponse(response=answer, sources=sources)
