from Question import Question

class CreatQuiz(Question):

    questionList = []

    def __init__(self,quizName):
        self.quizName = quizName
        
    def addQuestion(self,question,choices,answer):
        return self.questionList.append(Question(question,choices,answer))




