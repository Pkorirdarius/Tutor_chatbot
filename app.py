import streamlit as st
from streamlit_option_menu import option_menu
import time

# Set page configuration
st.set_page_config(page_title="AI Tutor", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for enhanced styling and transitions
st.markdown(
    """
    <style>
        .css-18e3th9 {
            background-color: #0d0d0d;
        }
        .stApp {
            background-color: #0d0d0d;
            color: white;
        }
        .stButton>button {
            background-color: #00a86b;
            color: white;
            border-radius: 10px;
            font-size: 18px;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #008b5e;
            transform: scale(1.05);
        }
        .stFileUploader div div button {
            background-color: #00a86b !important;
            color: white !important;
            border-radius: 10px !important;
            font-size: 18px !important;
            transition: all 0.3s ease-in-out;
        }
        .stFileUploader div div button:hover {
            background-color: #008b5e !important;
        }
        .upload-box {
            border: 2px dashed #00a86b;
            padding: 40px;
            text-align: center;
            border-radius: 10px;
            transition: all 0.3s ease-in-out;
        }
        .upload-box:hover {
            background-color: rgba(0, 168, 107, 0.1);
        }
        .fade-in {
            animation: fadeIn 1s ease-in;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown("<h1 style='text-align: center;' class='fade-in'>📄 AI Tutor</h1>", unsafe_allow_html=True)
st.write("Upload your PDFs and interact with an intelligent assistant that can answer questions, discuss content, provide summaries, and suggest reading paths.")

# File Uploader
uploaded_file = st.file_uploader("Upload your PDFs", type=["pdf"], accept_multiple_files=False)
if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")
    
    # Simulate a short delay for smooth transition
    time.sleep(0.5)
    
    # Interaction Modes (Only appear after file is uploaded)
    st.markdown("### Choose an Interaction Mode", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("💬 Question & Answer"):
            st.markdown("<p class='fade-in'>Ask specific questions about your documents and receive precise answers.</p>", unsafe_allow_html=True)
    
    with col2:
        if st.button("🎙 Active Discussion"):
            st.markdown("<p class='fade-in'>Have a voice conversation about your documents with the AI assistant.</p>", unsafe_allow_html=True)
    
    with col3:
        if st.button("📖 Document Briefing"):
            st.markdown("<p class='fade-in'>Get a comprehensive summary of your document's content and key points.</p>", unsafe_allow_html=True)
    
    with col4:
        if st.button("🔍 Reading Roadmap"):
            st.markdown("<p class='fade-in'>Follow a guided path through your document based on importance.</p>", unsafe_allow_html=True)
