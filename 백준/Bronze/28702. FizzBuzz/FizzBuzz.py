import sys

next = 0
a = sys.stdin.readline().rstrip('\n')
b = sys.stdin.readline().rstrip('\n')
c = sys.stdin.readline().rstrip('\n')

if a != 'Fizz' and a!='Buzz' and a!='FizzBuzz':
    next = int(a) + 3
if b != 'Fizz' and b!='Buzz' and b!='FizzBuzz':
    next = int(b) + 2
if c != 'Fizz' and c!='Buzz' and c!='FizzBuzz':
    next = int(c) + 1

if next % 3 == 0 and next % 5 == 0:
    print('FizzBuzz')
elif next % 3 == 0:
    print('Fizz')
elif next % 5 == 0:
    print('Buzz')
else:
    print(next)