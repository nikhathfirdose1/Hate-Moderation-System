import os
import ollama

import json



from src.workflow.models import ContextHateAnalysis


def analyse_hate(context: str, comment: str) -> bool:
    LLAMA_MODEL_SMALL = os.getenv("LLAMA_MODEL_SMALL", "llama3.2:3b")
    result = ollama.chat(
        model=LLAMA_MODEL_SMALL,
        messages=[{
            "role": "user",
            "content": ContextHateAnalysis(context, comment).build_prompt()
        }],
        
    )

    # print(json.dumps(result, indent=2))
    # print(result['message']['content'])

    # print("SHALLOW:", result['message']['content'].lower())

    return "true" in result['message']['content'].lower()
