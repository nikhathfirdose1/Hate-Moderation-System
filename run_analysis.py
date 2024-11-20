from dotenv import load_dotenv
from src.pipeline import perform


if __name__ == "__main__":
    load_dotenv('local.env')
    
    context = "In context of immigrants"
    comment = "Go back Home"
    print(perform(context, comment))