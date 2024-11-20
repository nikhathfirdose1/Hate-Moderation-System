# Imports
import dspy
import os

from src.dspy.models import ContextDeepHateAnalysis, ContextDeepHateWarning


def deep_hate_analysis(context: str, comment: str) -> bool:

    LLAMA_MODEL_LARGE = os.getenv("LLAMA_MODEL_LARGE", "llama2:13b")
    
    ollama_model = dspy.OllamaLocal(
        model=LLAMA_MODEL_LARGE,
        model_type='text',
        max_tokens=1000,
        temperature=0.1,
        top_p=0.8,
        frequency_penalty=1.17,
        top_k=40
    )
    
    # Configure the LLM model
    with dspy.settings.context(lm=ollama_model):
        result = dspy.ChainOfThought(ContextDeepHateAnalysis, max_retries=3).forward(
            context=context,
            comment=comment,
        )
        return result.output == "True"


def deep_hate_warning(context: str, comment: str) -> str:
    
    LLAMA_MODEL_LARGE = os.getenv("LLAMA_MODEL_LARGE", "llama2:13b")
    ollama_model = dspy.OllamaLocal(
        model=LLAMA_MODEL_LARGE,
        model_type='text',
        max_tokens=8000,
        temperature=0.1,
        top_p=0.8,
        frequency_penalty=1.17,
        top_k=40
    )
    
    # Configure the LLM model
    with dspy.settings.context(lm=ollama_model):
        result = dspy.ChainOfThought(ContextDeepHateWarning, max_retries=3).forward(
            context=context,
            comment=comment,
        )
        return result.output