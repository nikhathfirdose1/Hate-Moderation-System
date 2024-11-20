from dotenv import load_dotenv
from src.pipeline.analyse import hate_analysis
from src.pipeline.recommend import deep_hate_analysis, deep_hate_warning


def perform(context: str, comment: str)-> str:
    load_dotenv('../../local.env')
    
    hate = hate_analysis(context, comment)
    print(hate)
    if hate:
        deep_hate = deep_hate_analysis(context=context, comment=comment)
        print(deep_hate)
        if deep_hate:
            deep_warning = deep_hate_warning(context, comment)
            return deep_warning
    return None
