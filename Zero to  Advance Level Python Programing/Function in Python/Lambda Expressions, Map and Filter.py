
#def square(args): return args**2

numbers = [1,3,5,9]

square = lambda num: num**2
 
#result = list(map(square,numbers))

#result = list(lambda num: num**2, numbers)

result = square(3)

#for x in map(square,numbers):
 #   print(x)

#def checkEven(args): return args%2==0

checkEven = lambda x: x % 2 == 0

#result = list(filter(checkEven,numbers))

#result = list(filter(lambda x: x % 2 == 0,numbers))

result = checkEven(numbers[2])

print(result)