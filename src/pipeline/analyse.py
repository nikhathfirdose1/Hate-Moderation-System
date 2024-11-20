# Imports
import dspy
import os

from src.pipeline.models import ContextHateAnalysis


def hate_analysis(context: str, comment: str) -> bool:
    LLAMA_MODEL_SMALL = os.getenv("LLAMA_MODEL_SMALL", "llama3.2:3b")
    ollama_model = dspy.OllamaLocal(
        model=LLAMA_MODEL_SMALL,
        model_type='text',
        max_tokens=4000,
        temperature=0.1,
        top_p=0.8,
        frequency_penalty=1.17,
        top_k=40
    )

    # Configure the LLM model
    with dspy.settings.context(lm=ollama_model):
        result = dspy.ChainOfThought(ContextHateAnalysis, max_retries=3).forward(
            context=context,
            comment=comment,
        )
        return "true" in result.output.lower()
