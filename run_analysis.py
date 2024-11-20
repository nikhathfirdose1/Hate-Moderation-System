from dotenv import load_dotenv
from src.workflow import perform


if __name__ == "__main__":
    load_dotenv('local.env')
    
    context = "Manager to Employee"
    comment = "You are such a hardworker, taking all these breaks"
    print(perform(context, comment))