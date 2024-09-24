import sys

temp = []
for i in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())

    if a != 0:
        temp.append(a)
    else:
        temp.pop()

print(sum(temp))
