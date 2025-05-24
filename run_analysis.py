from dotenv import load_dotenv
# from src.dspy import perform_dspy
from src.workflow import perform


if __name__ == "__main__":
    load_dotenv('local.env')
    
    # context = "Told in context of sports where one team played the game well"
    # comment = "They Killed it"
    
    context = "Immigration"
    comment = "Go back to your country"
    
    # context = "Men Emotions supressed"
    # comment = "You shoudnt be crying like this"

    print(perform(context, comment))

