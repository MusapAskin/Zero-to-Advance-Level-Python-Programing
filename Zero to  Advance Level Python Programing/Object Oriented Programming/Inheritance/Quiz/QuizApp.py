from CreatQuiz import CreatQuiz
from Quiz import Quiz

q = CreatQuiz('Math')
q.addQuestion('2 x 2 = ?',['A):4','B):6','C):8','D):2'],4)
q.addQuestion('9 / 3 = ?',['A):1','B):3','C):7','D):9'],3)
q.addQuestion('2 + 10 = ?',['A):9','B):10','C):12','D):8'],12)

print(Quiz(q).load())