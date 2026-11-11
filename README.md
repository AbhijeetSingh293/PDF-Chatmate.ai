# 📄 PDF Chatmate – AI-Powered PDF Question Answering System

PDF Chatmate is an AI-powered document assistant that allows users to upload PDF files and ask questions in natural language. It uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from documents and generate context-aware answers using a Large Language Model (LLM).

Instead of manually searching through lengthy PDF documents, users can simply upload a document and interact with its content through a conversational interface.

## 🚀 Features

- **PDF Upload:** Upload PDF documents through an interactive interface.
- **Document Processing:** Extract and process text from uploaded PDFs.
- **Text Chunking:** Divide extracted text into smaller chunks for efficient retrieval.
- **Semantic Search:** Retrieve relevant document content using vector embeddings.
- **Vector Database:** Store and search document embeddings using ChromaDB.
- **AI-Powered Answers:** Generate natural language responses using Groq LLM.
- **Conversational Interface:** Ask questions about uploaded documents and receive relevant answers.
- **Context-Aware Responses:** Generate answers based on retrieved document information.

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| Programming Language | Python |
| PDF Processing | PyMuPDF |
| Embeddings | Sentence Transformers (MiniLM) |
| Vector Database | ChromaDB |
| LLM | Groq API |
| HTTP Requests | Requests |

## 🏗️ System Architecture

1. User uploads a PDF through the Streamlit frontend.
2. The frontend sends the PDF to the FastAPI backend.
3. The backend extracts text from the PDF using PyMuPDF.
4. Extracted text is divided into smaller chunks.
5. Text chunks are converted into vector embeddings.
6. Embeddings are stored in ChromaDB.
7. When a user asks a question, the system retrieves relevant document chunks.
8. The retrieved context is passed to the Groq LLM.
9. The LLM generates a relevant response, which is displayed in the frontend.

## 📂 Project Structure

```text
PDF-Chatmate/
│
├── backend/
│   ├── main.py
│   └── other backend modules
│
├── frontend.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/AbhijeetSingh293/PDF-Chatmate.ai.git
```

### 2. Navigate to the project directory

```bash
cd PDF-Chatmate.ai
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

Keep your API key private. Never upload your `.env` file to GitHub.

### 6. Start the FastAPI backend

Run the backend using Uvicorn (adjust the module path if your backend entry-point has a different name):

```bash
uvicorn backend.main:app --reload
```

The backend will be available at:

```text
http://localhost:8000
```

### 7. Start the Streamlit frontend

Open another terminal and run:

```bash
streamlit run frontend.py
```

Open the local URL displayed in your terminal to use PDF Chatmate.

## 💡 How to Use

1. Start the backend and frontend.
2. Open PDF Chatmate in your browser.
3. Upload a PDF document.
4. Click the **Index PDF** button.
5. Wait for document processing and indexing to complete.
6. Ask questions related to your uploaded PDF.
7. Receive AI-generated answers based on the retrieved document content.

## 🔮 Future Improvements

- Support multiple PDF documents.
- Improve retrieval accuracy using advanced embedding models.
- Add conversation history and session management.
- Support additional document formats.
- Improve answer evaluation and reduce hallucinations.
- Deploy the application to a cloud platform.

## 👨‍💻 Author

**Abhijeet Kumar Singh**

B.Tech – Computer Science and Engineering (AI & ML)

Sikkim Manipal Institute of Technology

GitHub: [AbhijeetSingh293](https://github.com/AbhijeetSingh293)

---

⭐ If you find this project useful, consider giving it a star!
