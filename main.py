from fastapi import FastAPI
from src.greet import Greet
from src.wavinghands import WavingHands
from src.chatbot.chatbot import ChatRequest,ChatBot

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, Docker! Again"}

@app.get("/health")
def health(greeting: str):
    print(f"Received greeting: {greeting}")
    return {"status": "healthy"}

@app.post("/greet")
def greet(request: Greet):
    wh = WavingHands(name=request.name)
    return {"message": wh.greet()}

@app.post("/chat")
def chat(request: ChatRequest):
    print(f"User requested::: {request.message}")
    firstChat = ChatBot()
    return firstChat.chat(request)