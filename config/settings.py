import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4o-mini"  # upgrade to gpt-5 when needed

VECTOR_DB_PATH = "data/vectorstore/faiss_index"
TEAM_CONTEXT_DIR = "data/team_context"
