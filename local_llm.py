# ollama_client_llm.py

from pandasai.llm.base import LLM
from ollama import Client


class OllamaClientLLM(LLM):
    def __init__(self, model="llama3", host="http://localhost:11434"):
        self.model = model
        self.client = Client(host=host)

    @property
    def type(self):
        return "ollama"

    def call(self, instruction, context=None) -> str:
        prompt = str(instruction)
        print(f"User prompt: {prompt}")

        response = self.client.chat(
            model=self.model, messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]
