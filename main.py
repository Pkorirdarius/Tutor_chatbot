import streamlit as st
import fitz  # PyMuPDF for PDF text extraction
import openai
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter as CharacterTextSplitter
import time

# Set OpenAI API Key
openai.api_key = "your_openai_api_key"  # Replace with your actual API key

# Set Streamlit Page Configuration
st.set_page_config(page_title="AI Tutor", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS Styling
st.markdown(
    """
    <style>
        .stApp { background-color: #0d0d0d; color: white; }
        .stButton>button { background-color: #00a86b; color: white; border-radius: 10px; font-size: 18px; transition: all 0.3s ease-in-out; }
        .stButton>button:hover { background-color: #008b5e; transform: scale(1.05); }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown("<h1 style='text-align: center;'>📄 AI Tutor</h1>", unsafe_allow_html=True)
st.write("Upload your PDFs and interact with an intelligent assistant.")

# File Upload
uploaded_file = st.file_uploader("Upload your PDFs", type=["pdf"], accept_multiple_files=False)

# Function to Extract Text from PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = "".join(page.get_text() for page in doc)
    return text

# Initialize AI Components
def create_ai_chain(text):
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    text_chunks = text_splitter.split_text(text)
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(text_chunks, embeddings)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    chain = ConversationalRetrievalChain.from_llm(ChatOpenAI(model_name="gpt-3.5-turbo"), vector_store.as_retriever(), memory=memory)
    return chain

# Conversation Handling
if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")
    text_content = extract_text_from_pdf(uploaded_file)
    chain = create_ai_chain(text_content)
    st.session_state["ai_chain"] = chain
    st.session_state["attempts"] = 0
    st.session_state["hint_shown"] = 0

    # User Chat Interface
    st.markdown("### Question & Answer Chatbot")
    user_question = st.text_input("Ask a question about the document:")

    if user_question:
        attempts = st.session_state["attempts"]
        hint_shown = st.session_state["hint_shown"]
        chain = st.session_state.get("ai_chain")
        response = chain.run(user_question)

        hints = ["Think about the main concept in the document.", "Consider the key points mentioned in the text."]

        if attempts < 2:
            st.warning(hints[hint_shown])
            st.session_state["hint_shown"] += 1
        else:
            st.success(f"Answer: {response}")

        st.session_state["attempts"] += 1
