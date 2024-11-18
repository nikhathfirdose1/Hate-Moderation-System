# Imports
import dspy
import os
from dotenv import load_dotenv
from typing import List

from pipeline.models import ContextHateExplaination

# # Load environment variables
# load_dotenv('../../local.env')

def explain_hate_context(context: List[str], comment: str) -> bool:
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
        result = dspy.ChainOfThought(ContextHateExplaination, max_retries=3).forward(
            context="\n".join(context),
            comment=comment,
        )
        return result.output
