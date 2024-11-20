import ollama

def check_if_hateful(hateful_comment, context):
    """
    Step 1: Check if the given comment is hateful or offensive in the specified context.
    """
    
    prompt = (
    f"Analyze the following statement: '{hateful_comment}' in the context of '{context}'. "
    f"Determine if this comment can be considered hateful, offensive, or harmful within this specific social, cultural, political, or sensitive context. "
    f"Take into account how different communities (e.g., racial, religious, gender-based, or marginalized groups) might perceive this comment based on their lived experiences or historical sensitivities. "
    f"Additionally, assess whether the comment contains sarcasm and whether that sarcasm changes its intent to something non-hateful in this context. "
    f"Be aware that certain phrases (e.g., 'They killed it' in a sports context) may appear harmful becuase of presence of word kill, but are actually harmless or positive depending on the context. "
    f"If the comment is not hateful in this context, respond with 'This comment is not considered hateful in this context.'"
)
    
   
    response = ollama.chat(
        model="llama2:13b",  
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["message"]["content"]

def generate_contextual_warning(hateful_comment, context):
    """
    Step 2: If the comment is deemed hateful, generate a warning message explaining why it can hurt certain communities in that specific context.
    """
    prompt = (
    f"Analyze the following statement: '{hateful_comment}' in the context of '{context}'. "
    f"Even if the statement does not contain explicit offensive language, evaluate how it could be interpreted as hurtful or offensive within this specific social, cultural, political, or sensitive context. "
    f"Focus on how it could affect one or two specific communities (e.g., racial, ethnic, religious, gender-based, or other marginalized groups) based on their historical experiences or societal challenges. "
    f"Consider how these communities might interpret the comment through the lens of their lived experiences, including issues like systemic discrimination, stereotypes, or cultural sensitivities. "
    f"If applicable, generate a concise warning message explaining why this statement could lead to negative consequences (e.g., public backlash or reputational harm) and hurt the sentiments of these specific groups.\n"
    f"The warning message should follow this format:\n"
    f"'This statement can hurt the sentiments of [inferred group/community]. Please avoid using such language to prevent misunderstandings or public backlash.'"
)
    
    
    response = ollama.chat(
        model="llama2:13b",  
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["message"]["content"]

if __name__ == "__main__":
    
   
    input_comment = input("Enter a potentially hurtful comment: ")
    input_context = input("Enter the context of this comment (e.g., social media debate, argument, etc.): ")
    
    
    result = check_if_hateful(input_comment, input_context)
    
    
    if "not considered hateful" in result:
        print(f"Result: {result}")
    

    else:
        warning_message = generate_contextual_warning(input_comment, input_context)
        print(f"Warning: {warning_message}")