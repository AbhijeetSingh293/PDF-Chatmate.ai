import os
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from backend.pdf_processor import extract_text_from_pdf, chunk_text
from backend.rag import index_chunks, query_rag
from backend.llm import generate_answer

app = FastAPI(title="PDF-Chatmate API")

UPLOAD_DIR = "./uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    text = extract_text_from_pdf(file_path)
    if not text.strip():
        raise HTTPException(status_code=400, detail="Could not extract readable text from PDF.")
        
    chunks = chunk_text(text)
    index_chunks(chunks, doc_name=file.filename)
    
    return {
        "filename": file.filename,
        "status": "Indexed successfully",
        "total_chunks": len(chunks)
    }

@app.post("/chat", response_model=QueryResponse)
async def chat_with_pdf(request: QueryRequest):
    context = query_rag(request.query)
    if not context:
        return QueryResponse(
            answer="No relevant content found in the uploaded documents.",
            sources=[]
        )
    answer = generate_answer(request.query, context)
    return QueryResponse(answer=answer, sources=context)

@app.get("/health")
def health_check():
    return {"status": "ok"}