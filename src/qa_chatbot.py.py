from transformers import pipeline
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

DB_PATH = "vector_db"

# Load embedding model (same as used during indexing)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS vector database
db = FAISS.load_local(DB_PATH, embeddings)
# Load FLAN model
pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def get_response(user_message):
    print("get_response called")
    docs_and_scores = db.similarity_search_with_score(user_message, k=1)

    if not docs_and_scores:
        return "Sorry, I don't have information about that."

    doc, score = docs_and_scores[0]

    print("Score:", score)

    if score > 1.5:
        return "Sorry, I don't have information about that."

    context = doc.page_content
    for line in context.split("\n"):
        if any(word in line.lower() for word in user_message.lower().split()):
            return line

    return context