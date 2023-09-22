from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
import os, sys
from dotenv import load_dotenv
import asyncio

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Running..."}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    print(data)
    user = data["user"]
    user_message = data["user_message"]
    temperature = data["temperature"]
    max_tokens = data["max_tokens"]
    response = await chatbot_response(user, user_message, temperature, max_tokens)
    return response

if __name__ == "__main__":
    asyncio.run(uvicorn.run(app, host="0.0.0.0", port=8000))