class HateAnalysis:
    def __init__(self, comment: str, context: str):
        self.comment = comment
        self.context = context

    def build_prompt(self) -> str:
        pass


class ContextHateAnalysis(HateAnalysis):
    def build_prompt(self) -> str:
        prompt = f"""
        Prompt for the Model:
        You are an extremely perceptive and context-aware assistant. Your task is to determine whether a comment is hateful or not, based on the given comment and its context. Analyze carefully using the following criteria:

        Understand the Context: Interpret the comment based on the provided context, as its meaning depends heavily on the situation.
        Positive Use of Hateful Words: If the comment contains generally hateful words, but they are used positively or neutrally (e.g., "They killed it" in sports), it is not hateful.
        Non-Hateful Words with Hateful Meaning: If the comment uses neutral words but conveys hate (e.g., "Go back home" in an immigration context), it is hateful.
        Sarcasm and Irony: Comments that use sarcasm, irony, or subtle mocking to demean or insult are considered hateful.
        Tone and Implication: Consider the tone and implications of the comment, not just the literal words.
        After analyzing the comment based on these rules, you must output only one word, either "True" or "False":

        Output "True" if the comment is hateful (even slightly).
        Output "False" if the comment is not hateful.
        Comment: {self.comment}
        Context: {self.context}

        Output: Only the word "True" or "False" — no explanations or reasoning.
        """
        return prompt


class ContextDeepHateAnalysis(HateAnalysis):
    def build_prompt(self) -> str:
        prompt = f"""
            Analyze the following comment: '{self.comment}' in the context: '{self.context}' for hate speech. Follow these steps carefully:

        1. Understand Context:
        Fully understand the {self.comment}'s intent within its {self.context}. Analyse whether it targets an individual or group based on identity, nationality, race, gender, or other protected characteristics.
        Determine if the comment promotes exclusion, marginalization, or questions someone's right to belong within the given {self.context}.

        2. Deeper Analysis:
        Evaluate whether the language used carries implicit bias, dehumanizing tones, or indirect hostility, even if no explicit slurs are present.
        Consider specific examples: phrases like "go back home" directed at an immigrant inherently promote exclusion and xenophobia and are considered hate speech.

        3. Sarcasm Check:
        Check if the tone is sarcastic, passive-aggressive, or coded to convey hate while appearing neutral. Pay attention to discriminatory undertones.
        Assess whether the comment fosters a hostility for a particular group.

        4. Results:
        Output True if:
        - The comment marginalizes or excludes based on identity, race, or other protected characteristics.
        - It promotes hate, xenophobia, or hostility in the given context.
        - The language implicitly or explicitly conveys discrimination or prejudice.

        Output False if:
        - The comment is neutral, positive, or contextually harmless.
        - It does not promote exclusion, hostility, or discrimination.

        Provide only "True" or "False" as the final output based on this analysis.
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
