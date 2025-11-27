from langchain_openai import ChatOpenAI
from config.prompts import RETRO_PROMPT

class RetrospectiveGenerator:

    def __init__(self, model="gpt-4o-mini"):
        self.llm = ChatOpenAI(model=model, temperature=0.2)

    def generate(self, user_input, rag_context=""):
        prompt = f"{RETRO_PROMPT}\n\nTeam Context:\n{rag_context}\n\nInput:\n{user_input}"
        return self.llm.invoke(prompt).content
