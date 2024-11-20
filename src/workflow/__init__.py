from src.workflow.analysis import analyse_hate
from src.workflow.deep_analysis import deep_analyse_hate
from src.workflow.warn import hate_reason


def perform(context: str, comment: str) -> str:
    hate = analyse_hate(context, comment)
    print(hate)
    if hate:
        deep_hate = deep_analyse_hate(context, comment)
        print(deep_hate)
        if deep_hate:
            deep_warning = hate_reason(context, comment)
            return deep_warning
    return None
