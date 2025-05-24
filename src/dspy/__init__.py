from src.dspy.analyse import hate_analysis
from src.dspy.recommend import deep_hate_analysis, deep_hate_warning


def perform_dspy(context: str, comment: str) -> str:
    hate = hate_analysis(context, comment)
    print(hate)
    if hate:
        deep_hate = deep_hate_analysis(context, comment)
        print(deep_hate)
        if deep_hate:
            deep_warning = deep_hate_warning(context, comment)
            return deep_warning
    return None
