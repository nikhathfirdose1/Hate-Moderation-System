class HateAnalysis:
    def __init__(self, comment: str, context: str):
        self.comment = comment
        self.context = context

    def build_prompt(self) -> str:
        pass


class ContextHateAnalysis(HateAnalysis):
    def build_prompt(self) -> str:
        prompt = f"""
        You are most sensitive person in the world. You are given a comment and the context of the conversation.
        Using the context and the comment, understand the whole meaning of the message and determine if you think the comment is hateful or not. 
        There are certain conditions to be considered before determining if the comment is hateful or not.
        - The comment might or might not contain the hatefull words.
        - If the comment contains the hatefull words, it might not be hateful. Its just the word used in a posive context and never conveyed hateful message. (e.g. 'They killed it' in a sports context is not hateful)
        - Even if the comment doesnt contain hatefull words in it, it doesnt mean it is not hateful. The comment might be hateful in a way that it is conveying with just non hateful words. (e.g. 'Go back home' in a immigrants context is hateful)
        - Sarcasm and irony are also to be considered as hate.
        
        This is the only information you have. You have to determine if the comment is hateful or not.
        
        Comment that needs to be analysed: {self.comment}
        Context of the conversation: {self.context}
        
        The warning message should follow this format: "True" even if the comment is slightly hateful else "False".
        *Output: Just the word 'True' or 'False'*
        """
        return prompt


class ContextDeepHateAnalysis(HateAnalysis):
    def build_prompt(self) -> str:
        prompt = f"""
        You are most sensitive person in the world. You are given a comment and the context of the conversation.
        Previous model has classified the comment as hateful. Keeping that on mind, you have to determine if the comment is really hateful or not.
        Using the context and the comment, understand the whole meaning of the message and tell me if the comment conveys hate or not. 
        There are certain conditions to be considered before determining if the comment is hateful or not.
        - The comment might or might not contain the hatefull words.
        - If the comment contains the hatefull words, it might not be hateful. Its just the word used in a posive context and never conveyed hateful message. (e.g. 'They killed it' in a sports context is not hateful)
        - Even if the comment doesnt contain hatefull words in it, it doesnt mean it is not hateful. The comment might be hateful in a way that it is conveying with just non hateful words. (e.g. 'Go back home' in a immigrants context is hateful)
        - Unserstand the sarcasm and irony in the comment. Sometimes the comment might be sarcastic and not hateful.
        - Understand the context and see if this comment effects any person/group/community in any specific way by keeping context in mind.
        
        
        This is the only information you have. You have to determine if the comment is hateful or not.
        
        Comment that needs to be analysed: {self.comment}
        Context of the conversation: {self.context}

        The warning message should follow this format: "True" even if the comment is hateful, "False" if not hateful. 
        *Output: Just the word 'True' or 'False'*
        """
        return prompt


class ContextDeepHateWarning(HateAnalysis):
    def build_prompt(self) -> str:
        prompt = f"""
        Comment that needs to be analysed: {self.comment}
        Context of the conversation: {self.context}
        
        Using the context and the comment, understand the whole meaning of the message and tell me if the comment conveys hate or not. 
        Even if the statement does not contain explicit offensive language, evaluate how it could be interpreted as hurtful or offensive within this specific social, cultural, political, or sensitive context. 
        Focus on how it could affect one or two specific communities (e.g., racial, ethnic, religious, gender-based, or other marginalized groups) based on their historical experiences or societal challenges. 
        Consider how these communities might interpret the comment through the lens of their lived experiences, including issues like systemic discrimination, stereotypes, or cultural sensitivities. 
        If applicable, generate a concise warning message explaining why this statement could lead to negative consequences (e.g., public backlash or reputational harm) and hurt the sentiments of these specific groups.
        
        The warning message should follow this format:
        'This statement can hurt the sentiments of [inferred group/community]. Please avoid using such language to prevent misunderstandings or public backlash.'
        """
        return prompt
