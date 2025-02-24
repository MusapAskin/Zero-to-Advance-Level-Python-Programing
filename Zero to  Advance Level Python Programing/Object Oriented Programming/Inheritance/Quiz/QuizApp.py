from CreatQuiz import CreatQuiz
from Quiz import Quiz

q = CreatQuiz('Math')
q.addQuestion('2 x 2 = ?',[4,6,8,2],4)
q.addQuestion('2 x 3 = ?',[2,5,7,6],6)
q.addQuestion('2 x 4 = ?',[9,3,8,1],8)

print(Quiz(q).load())