from pydantic import BaseModel

class Greet(BaseModel):
    message: str
    id: int
    name: str = None