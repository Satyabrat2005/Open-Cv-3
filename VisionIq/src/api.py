from fastapi import FastAPI
from pydantic import BaseModel
from query_engine import QueryEngine

app = FastAPI(
    title="VisionIQ API",
    description="Evidence-grounded video intelligence backend",
    version="1.0"
)
