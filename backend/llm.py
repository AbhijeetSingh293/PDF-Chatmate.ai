import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY", "")

# Point to Groq's OpenAI-compatible endpoint
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
) if api_key else None

def generate_answer(query: str, context_chunks: list[str]) -> str:
    if not client or not api_key:
        return "Groq API key is missing. Please set GROQ_API_KEY in your .env file."
    
    context_str = "\n\n".join(context_chunks)
    
    system_prompt = (
        "You are PDF-Chatmate, an intelligent document analysis assistant. "
        "Use the provided context to answer the user's question accurately. "
        "If the answer cannot be determined from the provided context, "
        "state that the document does not contain this information."
    )
    user_prompt = f"Context:\n{context_str}\n\nQuestion: {query}\n\nAnswer:"
    
    try:
        response = client.chat.completions.create(
            model=os.getenv("LLM_MODEL", "openai/gpt-oss-120b"),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error communicating with Groq API: {str(e)}"