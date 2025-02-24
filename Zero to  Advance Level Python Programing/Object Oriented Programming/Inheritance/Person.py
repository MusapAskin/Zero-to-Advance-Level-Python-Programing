from sqlite3 import Date


class Person():
    #Constructor method
    def __init__(self,name,lastName,birtYear,yearOfDeath):
        self.name = name
        self.lastName =  lastName
        self.birtYear = birtYear
        self.yearOfDeath = yearOfDeath
        
    #Special method
    def __str__(self):
        return f'Name: {self.name} {self.lastName}\nAge: {self.calculateAge()}\n'
    
    #Class method
    def calculateAge(self):
        if self.yearOfDeath==0:
           return Date.today().year - self.birtYear
        else:
           return f'{self.yearOfDeath - self.birtYear}\nDie: {self.yearOfDeath}'
    
    #Special method     
    def __del__(self):
        return f'{self.name} {self.lastName} deleted.\n'
