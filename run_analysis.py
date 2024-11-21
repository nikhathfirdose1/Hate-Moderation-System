from dotenv import load_dotenv
from src.workflow import perform


if __name__ == "__main__":
    load_dotenv('local.env')
    
    # context = "Told in context of sports where one team played the game well"
    # comment = "They Killed it "
    # print(perform(context, comment))
    
    # context = "Told to a guy"
    # comment = "Dont behave like a girl, be a man"
    
    context = "Consoling someone because they are hurt"
    comment = "You shoudnt be crying like this"
    print(perform(context, comment))