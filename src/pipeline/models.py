# Imports
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
        desc="""Strictly Tell "True" if hateful, "False" if not hateful.""",
    )
    
    
class ContextHateExplaination(dspy.Signature):
    """
    Using the context and the comment, understand the whole meaning of the message and tell me if the comment conveys hate or not. 
    There are certain conditions to be considered before determining if the comment is hateful or not.
    - The comment might or might not contain the hatefull words.
    - If the comment contains the hatefull words, it might not be hateful. Its just the word used in a posive context and never conveyed hateful message.
    - Even if the comment doesnt contain hatefull words in it, it doesnt mean it is not hateful. The comment might be hateful in a way that it is conveying with just non hateful words.
    - Unserstand the sarcasm and irony in the comment. Sometimes the comment might be sarcastic and not hateful.
    
    Understand the whole context and determine the result.
    
    Strictly Tell "False" if not hateful. 
    If hateful, provide the warning message in a format: "The comment is hateful as it is targetting [specific person/group/community] in a [specific way]."
    """

    comment: str = dspy.InputField()
    context: str = dspy.InputField()
    output = dspy.OutputField(
        desc="""Strictly Tell "False" if not hateful. If hateful, provide the warning message.""",
    )