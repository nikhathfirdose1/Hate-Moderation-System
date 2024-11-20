from dotenv import load_dotenv
from src.pipeline import perform


if __name__ == "__main__":
    load_dotenv('local.env')
    context = [
        "I love the way you are doing this.",
        "I dont know the way you are doing"]
    comment = "I dont like you"
    print(perform(context, comment))