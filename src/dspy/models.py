import dspy


class ContextHateAnalysis(dspy.Signature):
    """
    Using the context and the comment, understand the whole meaning of the message and tell me if the comment conveys hate or not. 
    There are certain conditions to be considered before determining if the comment is hateful or not.
    - The comment might or might not contain the hatefull words.
    - If the comment contains the hatefull words, it might not be hateful. Its just the word used in a posive context and never conveyed hateful message.
    - Even if the comment doesnt contain hatefull words in it, it doesnt mean it is not hateful. The comment might be hateful in a way that it is conveying with just non hateful words.
    - Sarcasm and irony are also to be considered as hate.
    - Classify as hateful if the comment is conveying hate even a little. Answer sensitively.  
    Understand the whole context and determine the result.   
    Output if the comment is Hateful or not. "True" if hateful, "False" if not hateful.
    """

    comment: str = dspy.InputField()
    context: str = dspy.InputField()
    output = dspy.OutputField(
        type=bool,
        desc="""If the comment in the context is hateful or not. "True" if command has hate, "False" if not.""",
    )


class ContextDeepHateAnalysis(dspy.Signature):
    """
    Using the context and the comment, understand the whole meaning of the message and tell me if the comment conveys hate or not. 
    There are certain conditions to be considered before determining if the comment is hateful or not.
    - The comment might or might not contain the hatefull words.
    - If the comment contains the hatefull words, it might not be hateful. Its just the word used in a posive context and never conveyed hateful message.
    - Even if the comment doesnt contain hatefull words in it, it doesnt mean it is not hateful. The comment might be hateful in a way that it is conveying with just non hateful words.
    - Unserstand the sarcasm and irony in the comment. Sometimes the comment might be sarcastic and not hateful.

    Understand the whole context and determine the result.

    Output: "True" if hateful, "False" if not hateful.
    """

    comment: str = dspy.InputField()
    context: str = dspy.InputField()
    output = dspy.OutputField(
        type=bool,
        desc="""If the comment in the context is hateful or not. "True" if command has hate, "False" if not.""",
    )


class ContextDeepHateWarning(dspy.Signature):
    """
    Even if the statement does not contain explicit offensive language, evaluate how it could be interpreted as hurtful or offensive within this specific social, cultural, political, or sensitive context.  There might be simple terms which can still portray hate.
    Focus on how it could affect one and sometimes two specific communities (e.g., racial, ethnic, religious, gender-based, LGBTQ+, socioeconomic, disability, age-based, immigration status, educational, cultural, linguistic, geographical, employment status, health status, legal status, indigenous, caste-based, and other systematically marginalized or underrepresented groups) 
    based on their historical experiences or societal challenges.
    Consider how these communities might interpret the comment through the lens of their lived experiences, including issues like systemic discrimination, stereotypes, or cultural sensitivities.
    Once you unserstand that how that comment is hurtful to the specific community generate a concise warning
    Give warning in this format: 'This statement can hurt the sentiments of [inferred group/community]. Please avoid using such language to prevent misunderstandings or public backlash that could lead to Celebrity Cancelling'
    """
    comment: str = dspy.InputField()
    context: str = dspy.InputField()
    output = dspy.OutputField(
        desc="""The message is hateful, thereby provide the warning message.""",
    )
