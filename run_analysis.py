from dotenv import load_dotenv
from src.workflow import perform


if __name__ == "__main__":
    load_dotenv('local.env')
    
    context = "Told in context of sports where one team played the game well"
    comment = "They Killed it "
    print(perform(context, comment))