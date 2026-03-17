import streamlit as st
import os
from data_loader import load_medquad_data

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

# Load dataset
data = load_medquad_data("data")
documents = data

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create vector database
vector_db = FAISS.from_documents(data, embedding_model)


# Streamlit UI
st.title("Medical Q&A Chatbot")

user_question = st.text_input("Ask a medical question:")

if user_question:

    results = vector_db.similarity_search(user_question, k=1)

    if results:
        st.write("Answer:")
        st.write(results[0].page_content)
    else:
        st.write("Sorry, I couldn't find an answer.")