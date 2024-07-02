import streamlit as st
import os
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()
os.environ["GOOGLE_KEY"] = os.getenv("GOOGLE_KEY")

# Directory to persist the index
PERSIST_DIR = "./storage"

# Streamlit app title
st.title("PDF QNA")

# File uploader for adding new PDF documents
uploaded_files = st.file_uploader(
    "Upload PDF files", accept_multiple_files=True, type=["pdf"]
)

if uploaded_files:
    data_dir = Path("data")
    data_dir.mkdir(parents=True, exist_ok=True)

    for uploaded_file in uploaded_files:
        file_path = data_dir / uploaded_file.name
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    st.success("Files uploaded successfully. Please refresh to update the index.")

# Check if the persist directory exists
if not os.path.exists(PERSIST_DIR):
    st.write("Index does not exist. Creating a new index...")

    # Load documents from the 'data' directory
    documents = SimpleDirectoryReader("data").load_data()

    # Create a VectorStoreIndex from the documents
    index = VectorStoreIndex.from_documents(documents)

    # Persist the index to disk
    index.storage_context.persist(persist_dir=PERSIST_DIR)
    st.write("Index created and persisted.")
else:
    st.write("Loading existing index from storage...")

    # Load the index from the existing storage context
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)
    st.write("Index loaded from storage.")

# Create a query engine from the index
query_engine = index.as_query_engine()

# Streamlit input for the query
query = st.text_input("Enter your query:", "")

# If the query is not empty, execute it and display the response
if query:
    response = query_engine.query(query)
    st.write("Response:")
    st.write(response.response)
