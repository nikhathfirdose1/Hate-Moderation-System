from dotenv import load_dotenv
from pipeline.analyse import determine_hate
from pipeline.recommend import explain_hate_context



def perform(context: str, comment: str)-> bool:
    load_dotenv('../../local.env')
    
    if determine_hate(context, comment):
        print("Hate detected")
        return explain_hate_context(context, comment)
    return False


if __name__ == "__main__":
    context = [
        "I love the way you are doing this.",
        "I dont know the way you are doing"]
    comment = "I hate the way you are doing this."
    print(perform(context, comment))