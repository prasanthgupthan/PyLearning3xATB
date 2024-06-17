# fina a maximum number from 3 output

n1 = int(input('Enter a number1: '))
n2 = int(input('Enter a number2: '))
n3 = int(input('Enter a number3: '))

if n1 > n2 and n1 > n3:
    print('n1 is maximum')
elif n2 > n3:
    print('n2 is maximum')
else:
    print('n3 is maximum')