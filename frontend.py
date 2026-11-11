import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(page_title="PDF-Chatmate", page_icon="📄", layout="wide")
st.title("📄 PDF-Chatmate")

with st.sidebar:
    st.header("Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    if uploaded_file is not None:
        if st.button("Index PDF"):
            with st.spinner("Processing & Indexing..."):
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                try:
                    res = requests.post(f"{BACKEND_URL}/upload", files=files)
                    if res.status_code == 200:
                        st.success(f"Indexed: {res.json().get('total_chunks')} chunks")
                    else:
                        st.error(res.json().get("detail", "Upload failed"))
                except Exception as e:
                    st.error(f"Could not connect to backend: {e}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question about your PDF:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                res = requests.post(f"{BACKEND_URL}/chat", json={"query": prompt})
                if res.status_code == 200:
                    data = res.json()
                    answer = data.get("answer", "")
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                else:
                    st.error("Error getting response from backend.")
            except Exception as e:
                st.error(f"Connection failed: {e}")