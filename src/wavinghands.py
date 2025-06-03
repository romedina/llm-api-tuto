class WavingHands:
    def __init__(self, name: str):
        self.name = name

    def wave(self):
        return f"{self.name} is waving hands!"

    def greet(self):
        if(self.name == "Kevin"):
            return f"{self.name} you know the secret greeting!"
        else:
            return f"{self.name} says hello!"