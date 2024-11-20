# Imports
import dspy
import os
from dotenv import load_dotenv
from typing import List

from src.pipeline.models import ContextDeepHateAnalysis, ContextDeepHateWarning

# # Load environment variables
# load_dotenv('../../local.env')

def deep_hate_analysis(context: List[str], comment: str) -> bool:
    load_dotenv('../../local.env')

    # Get model name
    GROQ_MODEL_LARGE = os.environ['GROQ_MODEL_LARGE']

    # Configure the LLM model
    with dspy.settings.context(
        lm=dspy.LM(model=f"groq/{GROQ_MODEL_LARGE}", 
            max_tokens=8000, 
            cache=False,
        ),
        temperature=0,
    ):
        result = dspy.ChainOfThought(ContextDeepHateAnalysis, max_retries=3).forward(
            context="\n".join(context),
            comment=comment,
        )
        return "true" in result.output.lower()


def deep_hate_warning(context: List[str], comment: str) -> str:
    load_dotenv('../../local.env')

    # Get model name
    GROQ_MODEL_LARGE = os.environ['GROQ_MODEL_LARGE']

    # Configure the LLM model
    with dspy.settings.context(
        lm=dspy.LM(model=f"groq/{GROQ_MODEL_LARGE}", 
            max_tokens=8000, 
            cache=False,
        ),
        temperature=0,
    ):
        result = dspy.ChainOfThought(ContextDeepHateWarning, max_retries=3).forward(
            context="\n".join(context),
            comment=comment,
        )
        return result.output