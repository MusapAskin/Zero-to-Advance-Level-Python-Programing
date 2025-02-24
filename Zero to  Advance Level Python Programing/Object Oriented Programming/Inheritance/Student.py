from Person import Person

class Student(Person):

    #Override constructor
    def __init__(self,name,lastName,birtYear,yearOfDeath,studentNumber):
        Person.__init__(self,name,lastName,birtYear,yearOfDeath)
        self.studentNumber = studentNumber
    
    #Override
    def __str__(self):
        return f'Name: {self.name} {self.lastName}\nAge: {self.calculateAge()}\nStudent Number: {self.studentNumber}\n'
    
    #Class method
    def study(self,subject):
        return f'{self.name} studied {subject}.\n'

    #Override
    def __del__(self):
        return f'{self.studentNumber} {self.name} {self.lastName} deleted.\n'
