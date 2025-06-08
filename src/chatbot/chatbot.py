from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class ChatRequest(BaseModel):
    message: str

class ChatBot:
    def __init__(self):
        self.model_name = "microsoft/DialoGPT-medium"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)

    def chat(self, request: ChatRequest):
        prompt = (
        "You are a friendly and helpful assistant. The user asks you something and you respond with detail.\n\n"
        f"User: {request.message}\nAssistant:"
        )
        print(prompt)
        print("Processing the following...")
        inputs = self.tokenizer(prompt, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_length=100,
                temperature=0.7,
                top_k=50,
                top_p=0.9,
                repetition_penalty=1.2,
                pad_token_id=self.tokenizer.eos_token_id
            )
        response_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(response_text)
        # Extract the assistant's response after the prompt
        if "Assistant:" in response_text:
            response_text = response_text.split("Assistant:")[-1].strip()
        return {"response": response_text}