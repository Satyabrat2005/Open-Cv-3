from fastapi import FastAPI
from pydantic import BaseModel
from query_engine import QueryEngine

app = FastAPI(
    title="VisionIQ API",
    description="Evidence-grounded video intelligence backend",
    version="1.0"
)

engine = QueryEngine(top_k=5, use_llm=True)


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    question: str
    answer: str
    results: list

@app.post("/query", response_model=QueryResponse)
def query_video(request: QueryRequest):
    response = engine.query(request.question)
    return response
