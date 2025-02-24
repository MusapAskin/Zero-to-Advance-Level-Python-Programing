from Student import Student
from Person import Person


student = Student('Musap','Askin',1998,0,1298)
person = Person('Baris','Manco',1943,1999)

print(student)

print(person)

print(student.study('Math'))

print(person.__del__())

print(student.__del__())