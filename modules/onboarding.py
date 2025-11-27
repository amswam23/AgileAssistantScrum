from langchain_openai import ChatOpenAI
from config.prompts import ONBOARDING_PROMPT

class OnboardingGenerator:

    def __init__(self, model="gpt-4o-mini"):
        self.llm = ChatOpenAI(model=model, temperature=0.2)

    def generate(self, role, rag_context=""):
        prompt = f"{ONBOARDING_PROMPT}\n\nRole: {role}\n\nTeam Context:\n{rag_context}"
        return self.llm.invoke(prompt).content
