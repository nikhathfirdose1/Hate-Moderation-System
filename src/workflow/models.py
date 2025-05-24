class HateAnalysis:
    def __init__(self, comment: str, context: str):
        self.comment = comment
        self.context = context

    def build_prompt(self) -> str:
        pass


class ContextHateAnalysis(HateAnalysis):
    def build_prompt(self) -> str:
        prompt = f"""
        You are a quick, sensitive classifier that flags comments that may be hateful, discriminatory, emotionally invalidating, or implicitly hostile **within the given context**.

        You are not making a final judgment — just a surface-level flag. Be conservative and cautious. If the comment uses exclusionary language or aggressive tone, flag it.

        Important: Always flag comments that mention identity, race, nationality, gender, or emotional suppression — even subtly.

        Return "True" if the comment seems potentially hateful or problematic.
        Return "False" only if the comment is clearly supportive, neutral, or contextually harmless.

        Examples:

        Context: "Immigration"
        Comment: "Go back to your country"
        Output: True

        Context: "Sports"
        Comment: "They killed it"
        Output: True

        Context: "Men's emotions debate"
        Comment: "You shouldn't be crying like this"
        Output: True

        Context: "Friend consoling another after injury"
        Comment: "You shouldn't be crying like this"
        Output: True

        Context: "Encouraging someone"
        Comment: "You can do better next time"
        Output: False

        Context: "Gaming chat"
        Comment: "You suck!"
        Output: True

        Context: "Academic feedback"
        Comment: "Your writing needs improvement"
        Output: False

        Now evaluate:

        Context: "{self.context}"
        Comment: "{self.comment}"

        Output: Only the word "True" or "False".
        """
        return prompt



class ContextDeepHateAnalysis(HateAnalysis):
    def build_prompt(self) -> str:
        prompt = f"""
        You are a highly context-aware assistant trained to detect hate speech, emotional harm, and social discrimination. Your job is to evaluate the intent and impact of a comment **in the specific context provided**.

        Follow these rules:

        1. Understand the context: Is this a sensitive topic? (e.g., immigration, race, gender, mental health)
        2. Examine the comment: Is it hostile, demeaning, emotionally suppressive, exclusionary, or mocking?
        3. If the comment promotes exclusion, prejudice, or harmful stereotypes — it is hateful.

        Key rule: Do NOT overlook hate speech related to **nationality, identity, or race**, even if it uses neutral words.

        Return only one word: "True" or "False"

        ### Examples:

        Context: "Immigration"
        Comment: "Go back to your country"
        Output: True

        Context: "Sports"
        Comment: "They killed it"
        Output: False

        Context: "Debate about men's emotional suppression"
        Comment: "You shouldn't be crying like this"
        Output: True

        Context: "Consoling a friend"
        Comment: "You shouldn't be crying like this"
        Output: False

        Context: "Casual gaming banter"
        Comment: "You suck!"
        Output: False

        ### Now evaluate:

        Context: "{self.context}"
        Comment: "{self.comment}"

        Output:
        """
        return prompt



class ContextDeepHateWarning(HateAnalysis):
    def build_prompt(self) -> str:
        prompt = f"""
        Once the {self.comment} is classified as Hateful
        Analyse why the Comment is Hateful:
        Based on the input context, explain why the comment is considered hateful based on the given {self.context}. Identify if it uses explicit hate speech, implicit bias, sarcasm, or derogatory tones that target specific ideas, identities, or behaviors.
        Affected Groups/Communities:
        In the given context, analyze which groups or communities could be hurt by this comment. Consider factors such as:
        The nature of the discussion (e.g., gender equality, race relations, political ideologies, LGBTQ community, Religion, ).
        The groups explicitly or implicitly referenced in the comment.
        The broader societal implications of such statements.
        Potential Consequences:
        Evaluate what could happen if such comments continue to be used. Include possible outcomes like:
        Emotional harm or alienation of individuals/groups.
        Public backlash or reputational damage for the user.
        Escalation of tensions in sensitive discussions.
        Contribution to systemic issues like discrimination or harassment.
        Final Warning to User:
        Provide a clear and sensitive two-sentence warning that highlights the harm caused by such language and advises against its use to prevent further consequences.
        Give warning in this format: 'We understand that you may hold different beliefs and values, but the statement you are trying to make can hurt the sentiments of an individual based on the given context. Please avoid using such language to prevent misunderstandings or public backlash.'

        Just output the warning to user starting from 'We undersatand.. format'
        """
        return prompt
