from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from ai_agent import get_response_from_aiagent

app = FastAPI(title="Crypto Analyst AI")

class RequestData(BaseModel):
    model_id: str
    system_prompt: str
    allow_search: bool
    messages: List[str]

@app.get("/")
def root():
    return {"message": "Crypto Analyst AI API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(request: RequestData):
    if request.model_id not in ["llama3-70b-8192", "mixtral-8x7b-32768"]:
        raise HTTPException(status_code=400, detail="Invalid model")

    if not request.messages:
        raise HTTPException(status_code=400, detail="No message provided")

    query = request.messages[-1]
    response = get_response_from_aiagent(
        model_id=request.model_id,
        allow_search=request.allow_search,
        system_prompt=request.system_prompt,
        query=query
    )

    return {
        "response": response,
        "model_used": request.model_id,
        "search_enabled": request.allow_search
    }
