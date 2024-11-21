import os
import ollama

from src.workflow.models import ContextDeepHateWarning


def hate_reason(context: str, comment: str) -> str:
    LLAMA_MODEL_LARGE = os.getenv("LLAMA_MODEL_LARGE", "llama3.2:3b")
    result = ollama.chat(
        model=LLAMA_MODEL_LARGE,
        messages=[{
            "role": "user",
            "content": ContextDeepHateWarning(context, comment).build_prompt()
        }],
    )
    
    return result['message']['content']
