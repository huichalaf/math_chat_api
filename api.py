from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
import os, sys
from dotenv import load_dotenv
import asyncio
import uvicorn
from main import chat
from db import auth_user

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Running..."}

@app.post("/chat")
async def chat_(request: Request):
    data = await request.json()
    print(data)
    user = data["user"]
    token = data["token"]
    message = data["message"]
    temperature = data["temperature"]
    max_tokens = data["max_tokens"]
    if not await auth_user(user, token):
        return {"user": user, "message": "Invalid token"}
    try:
        response = await chat(user, message, temperature, max_tokens)
    except:
        return {"user": user, "message": "Error in chat"}
    state_chart = response[1]
    response_text = response[0]
    if state_chart:
        try:
            imagen = await imagen_a_bytesio(f"{files_path}images/{user}.png")
            imagen_base64 = base64.b64encode(imagen).decode("utf-8")
        except Exception as e:
            return {"user": user, "message": response_text, "image": None}
        return {"user": user, "message": response_text, "image": imagen_base64}
        
    else:
        return {"user": user, "message": response_text, "image": None}

if __name__ == "__main__":
    asyncio.run(uvicorn.run(app, host="0.0.0.0", port=8000))