# Imports
import dspy
import os
from dotenv import load_dotenv
from typing import List

from pipeline.models import ContextHateAnalysis

# # Load environment variables
# load_dotenv('../../local.env')



def determine_hate(context: List[str], comment: str) -> bool:
    load_dotenv('../../local.env')

    # Get model name
    GROQ_MODEL_SMALL = os.environ['GROQ_MODEL_SMALL']
    
    # Configure the LLM model
    with dspy.settings.context(
        lm=dspy.LM(model=f"groq/{GROQ_MODEL_SMALL}", 
            max_tokens=8000, 
            cache=False
        ),
        temperature=0,
    ):
        result = dspy.ChainOfThought(ContextHateAnalysis, max_retries=3).forward(
            context="\n> ".join(context),
            comment=comment,
        )
        return "true" in result.output.lower()
