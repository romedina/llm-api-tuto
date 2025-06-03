from fastapi import FastAPI
from src.greet import Greet
from src.wavinghands import WavingHands

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, Docker! Again"}

@app.post("/health")
def health(greeting: str):
    print(f"Received greeting: {greeting}")
    return {"status": "healthy"}

@app.post("/greet")
def greet(request: Greet):
    wh = WavingHands(name=request.name)
    return {"message": wh.greet()}