import sys

def push(stack, item):
    stack.append(item)

def top(stack):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

def empty(stack):
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def size(stack):
    print(len(stack))

stack = []
for i in range(int(sys.stdin.readline())):
    userInput = sys.stdin.readline().rstrip('\n')

    if userInput == 'top':
        top(stack)
    elif userInput == 'size':
        size(stack)
    elif userInput == 'empty':
        empty(stack)
    elif userInput == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif 'push' in userInput:
        push(stack, userInput.split()[1])

