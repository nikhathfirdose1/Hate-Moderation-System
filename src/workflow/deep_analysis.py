import os
import ollama

from src.workflow.models import ContextDeepHateAnalysis


def deep_analyse_hate(context: str, comment: str) -> bool:
    LLAMA_MODEL_LARGE = os.getenv("LLAMA_MODEL_LARGE", "llama3.2:3b")
    result = ollama.chat(
        model=LLAMA_MODEL_LARGE,
        messages=[{
            "role": "user",
            "content": ContextDeepHateAnalysis(context, comment).build_prompt()
        }],
        options={'temperature': 0.1, 'top_p': 0.8,
                 'frequency_penalty': 1.17, 'top_k': 40, 'max_tokens': 8000}
    )

    return "true" in result['message']['content'].lower()
