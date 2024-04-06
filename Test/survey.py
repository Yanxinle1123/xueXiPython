class AnonymousSurvey:
    """收集调查问题的匿名答案"""

    def __init__(self, question):
        """存储问题，并准备存储答案"""

        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问题"""

        print(self.question)

    def store_response(self, new_response):
        """存储对调查的单个答复"""

        self.responses.append(new_response)

    def show_results(self):
        """已给出的所有答复如何"""

        print("调查结果:")
        for response in self.responses:
            print(f"- {response}")
