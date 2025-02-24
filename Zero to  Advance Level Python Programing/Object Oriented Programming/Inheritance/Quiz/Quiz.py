from CreatQuiz import CreatQuiz

class Quiz(CreatQuiz):
    def __init__(self,quiz):
        self.quiz = quiz
        self.score = 0
        self.index = 0

    def getQuestion(self):
        return print(f'Question {self.index+1}: {self.quiz.questionList[self.index].question}\n')
        
   
    def getChoices(self):
        return list(map(print, self.quiz.questionList[self.index].choices))
        

    def start(self):
        self.getQuestion()
        self.getChoices()
        self.choice(input('\nAnswer: '))
        self.load()
        
        
    def choice(self,answer):
        if str(self.quiz.questionList[self.index].answer)==answer:
            self.score +=1
        self.index +=1
        
       
    def progress(self):
        if len(self.quiz.questionList) < (self.index+1):
            return print(' # Game Over # '.center(100,'-'))
        else:
           return print(f' {self.quiz.quizName} question {self.index+1} / {len(self.quiz.questionList)} '.center(100,'-'),'\n')
      

    def load(self):
        if len(self.quiz.questionList) == self.index:
             self.progress()
             self.showScore()
        else:
            self.progress()
            self.start()
           
        return ''.center(100,'-')

    def showScore(self):
        return print(f'Score: {self.score}'.center(100,' '))
