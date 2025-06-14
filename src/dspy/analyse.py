# Imports
from click import prompt
import dspy
import os

from litellm import ollama_models
import ollama

from src.dspy.models import ContextHateAnalysis


def hate_analysis(context: str, comment: str) -> bool:
    LLAMA_MODEL_SMALL = os.getenv("LLAMA_MODEL_SMALL", "llama3.2:3b")
    ollama.chat(
        model="llama2:13b",  
        messages=[{"role": "user", "content": prompt}]
    )

    # Configure the LLM model
    with dspy.settings.context(lm=ollama_models):
        result = dspy.ChainOfThought(ContextHateAnalysis, max_retries=3).forward(
            context=context,
            comment=comment,
        )
        return result.output == "True"
