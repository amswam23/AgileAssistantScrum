import streamlit as st
from modules.rag_engine import RAGEngine
from modules.retrospective import RetrospectiveGenerator
from modules.onboarding import OnboardingGenerator
from langchain_openai import ChatOpenAI
from config.prompts import QA_PROMPT

st.set_page_config(page_title="AI Agile Assistant", layout="wide")
st.title("🤖 AI-Powered Agile Assistant")

rag = RAGEngine()
rag.load_vectorstore()

tab1, tab2, tab3 = st.tabs(["Retrospective Generator", "Team Onboarding", "Ask Agile Coach"])

# ---- Retrospective ----
with tab1:
    st.header("📝 Sprint Retrospective Analyzer")
    user_input = st.text_area("Paste sprint feedback / Jira export / Slack notes")
    
    if st.button("Generate Retrospective"):
        gen = RetrospectiveGenerator()
        context = rag.query("team norms and past retrospectives")
        output = gen.generate(user_input, context)
        st.write(output)

# ---- Onboarding ----
with tab2:
    st.header("🚀 Team Onboarding Assistant")
    role = st.text_input("Enter role (e.g., Backend Engineer, QA, Scrum Master)")

    if st.button("Generate Onboarding Plan"):
        gen = OnboardingGenerator()
        context = rag.query("onboarding and team structure")
        output = gen.generate(role, context)
        st.write(output)

# ---- Ask Agile Coach ----
with tab3:
    st.header("🧠 Ask an Agile Coach")
    question = st.text_input("Ask anything about Agile, SAFe, Scrum, DevOps, Delivery, Team management")

    if st.button("Ask"):
        llm = ChatOpenAI(model="gpt-4o-mini")
        full_prompt = f"{QA_PROMPT}\n\nQuestion: {question}"
        answer = llm.predict(full_prompt)
        st.write(answer)
