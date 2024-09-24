import sys

for i in range(int(sys.stdin.readline())):
    temp = []
    a = sys.stdin.readline().rstrip('\n')
    if a == '.':
        break

    k = 'YES'
    for i in a:
        if i == '(' or i == '[':
            temp.append(i)
        elif i == ')':
            if len(temp) == 0:
                k = 'NO'
                break
            elif temp[-1] != '(':
                k = 'NO'
                break
            else:
                temp.pop()
        elif i == ']':
            if len(temp) == 0:
                k = 'NO'
                break
            elif temp[-1] != '[':
                k = 'NO'
                break
            else:
                temp.pop()

    if len(temp) != 0:
        k = 'NO'
    print(k)
