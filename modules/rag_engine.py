import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from config.settings import TEAM_CONTEXT_DIR, VECTOR_DB_PATH

class RAGEngine:

    def __init__(self):
        self.embedding = OpenAIEmbeddings()
        self.vstore = None

    def load_vectorstore(self):
        if os.path.exists(VECTOR_DB_PATH):
            try:
                self.vstore = FAISS.load_local(VECTOR_DB_PATH, self.embedding, allow_dangerous_deserialization=True)
                return
            except Exception as e:
                print("Failed to load FAISS index, rebuilding:", e)

        self.build_vectorstore()

    def build_vectorstore(self):
        texts = []

        if not os.path.exists(TEAM_CONTEXT_DIR):
            os.makedirs(TEAM_CONTEXT_DIR)

        # load only .txt files
        for file in os.listdir(TEAM_CONTEXT_DIR):
            path = os.path.join(TEAM_CONTEXT_DIR, file)

            if not file.lower().endswith(".txt"):
                continue

            with open(path, "r") as f:
                content = f.read().strip()
                if content:   # skip empty files
                    texts.append(content)

        # SAFETY GUARD
        if len(texts) == 0:
            print("No context files found. Creating empty vectorstore.")
            # create dummy minimal vectorstore
            texts = ["Team context unavailable."]  

        self.vstore = FAISS.from_texts(texts, self.embedding)
        self.vstore.save_local(VECTOR_DB_PATH)

    def query(self, question):
        if not self.vstore:
            return ""
        docs = self.vstore.similarity_search(question, k=3)
        return "\n\n".join([d.page_content for d in docs])
