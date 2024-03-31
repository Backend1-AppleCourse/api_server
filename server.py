from fastapi import FastAPI, Query
from typing import Optional
from routes.db import router as students
from src.logging_http_middleware import LogRequestsMiddleware

app = FastAPI()

app.include_router(students)

# Add logging middleware
app.add_middleware(LogRequestsMiddleware)

# Root or home endpoint
@app.get("/")
async def read_root():
    return {"Hello": "World"}