import pymupdf as fitz
from typing import List, Dict

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extracts raw text content from a PDF document."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

def chunk_text(text: str, chunk_size: int = 500, chunk_overlap: int = 50) -> List[Dict[str, str]]:
    """Splits plain text into overlapping word chunks for vector embedding."""
    words = text.split()
    chunks = []
    
    if not words:
        return chunks
        
    start = 0
    chunk_id = 0
    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        chunks.append({
            "chunk_id": str(chunk_id),
            "text": " ".join(chunk_words)
        })
        start += chunk_size - chunk_overlap
        chunk_id += 1

    return chunks