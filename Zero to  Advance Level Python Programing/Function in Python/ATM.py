
class BankAccount:
    def __init__(self,name,password):
        self.name=name
        self.password=password
        self.balance=0

    def __str__(self):
        return f"********** Welcome Mr.{self.name} **********\n  Your account details:\n\t\t\tUser Name: {self.name}\n\t\t\tAmount: {self.balance}"
    
    def addMoney(self,amount):
        self.balance += amount
        self.showBalance()

    def drawMoney(self,amount):
        if self.balance >= amount:
            print('Money was withdrawn...')
            self.balance -=amount
            self.showBalance()

        else:
            print('You dont have enough money in your account.')
    
    def showBalance(self):
        print(f"Balance: {self.balance}")



def atm():
    
    def creatAccount():
        name=input('Enter your name: ')
        password=input('Creat password: ')
        return BankAccount(name,password)

    def money():
        value = int(input('1.Enter account\n2.Quit\n\nChoice: '))
        if value ==1:
            name = str(input('Enter your account name: '))
            password = str(input('Enter your password: '))
            
            if name == str(accountName.name) and str(accountName.password) == password:
                print(f'{accountName}\n1.Add Money\n2.Draw Money\n3.Quit\n')
                while True:
                    key = int(input('Please select:'))
                    if key ==1:
                        amount = int(input('How much do you want to add ?\n'))
                        accountName.addMoney(amount)
                    if key ==2:
                        amount = int(input('How much do you want to draw ?\n'))
                        accountName.drawMoney(amount)
                    if key==3:
                        print('Thank you for using ATM. Good By...')
                        break
            else:
                print('\033[31m Wrong name or password! \033[0m Try again...\n')
                money()
        if value==2:
            print('Thank you for using ATM. Good By...')

    print('********** Creat Account **********') 
    accountName=creatAccount()  
    money()
    
           
atm()
     