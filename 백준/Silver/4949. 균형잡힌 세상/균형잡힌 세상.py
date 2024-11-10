import sys

while True:
    temp = []
    a = sys.stdin.readline().rstrip('\n')
    if a == '.':
        break

    k = 'yes'
    for i in a:
        if i == '(' or i == '[':
            temp.append(i)
        elif i == ')':
            if len(temp) == 0:
                k = 'no'
                break
            elif temp[-1] != '(':
                k = 'no'
                break
            else:
                temp.pop()
        elif i == ']':
            if len(temp) == 0:
                k = 'no'
                break
            elif temp[-1] != '[':
                k = 'no'
                break
            else:
                temp.pop()

    if len(temp) != 0:
        k = 'no'
    print(k)
