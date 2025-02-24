import datetime

def calculateAge(birtYear):
    if int(birtYear) <= 1850:
        return "Your birtyear is \033[31m'to small'\033[0m. Please enter the year bigger than 1850."
        
    return 'You are ' + str(datetime.datetime.now().year - int(birtYear)) + ' years old.'

#print(calculateAge('1850'))
#print(calculateAge('1998'))

# 1 - G�nderilen bir kelimeyi belirtilen kes ekranda g�steren fonksiyonu yaz�n.
def repeatSentence(sentence, repeat):
    return (str(sentence) + '\n') * int(repeat)

#print(repeatSentence('musap',5))

# 2 - Kendine g�nderilen s�n�rs�z say�daki parametreyi bir listeye �eviren fonksiyonu yaz�n.
def convertList(*args):
    list = []
    for x in args:
         list.append(x)
    return list

#print(convertList('Musap','Askin',27))

# 3 - G�nderilen 2 say� aras�ndaki t�m asal say�lar� bulun.
def primeNumber():
    n1=int(input('number1: '))
    n2=int(input('number2: '))
    print(f'Prime numbers in between {n1} and {n2} is: ')
    for number in range(n1, n2 + 1):
        if number > 1:
            for i in range(2,number):
                if (number % i)==0:
                    break
            else:
                print(number)


#primeNumber()
           
# 4 - Kendisine g�nderilen bir say�n�n tam b�lenlerini bir liste �eklinde d�nd�r�n.
def fullDivisors():
    number = int(input('Number: '))
    print(f'Full divisors of {number} is : ')
    divisors = []
    for n in range(1,number + 1):
        if (number%n)==0:
            divisors.append(n)
    print(divisors)

#fullDivisors()

def prime():
     number = int(input('Enter number:'))
     if  number > 1:
         for n in range(2,number):
             if number%n==0:
                 print(f'{number} is not prime.\n')
                 break
         else:
              print(f'{number} is prime.\n')            
     else:
          print('Please enter a number bigger then one.\n')
     print('(Quit: -1)\n')
     while (number==-1):
         print('Exiting...')
         break
     else:
         prime()

