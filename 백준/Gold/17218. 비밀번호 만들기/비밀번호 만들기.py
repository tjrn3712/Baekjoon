import sys
from collections import deque
import math
ipt = sys.stdin.readline

a = list(ipt().rstrip('\n'))
b = list(ipt().rstrip('\n'))
lis = [[0] * (len(a)+1) for i in range(len(b)+1)]
m = 0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:

            lis[j+1][i+1] = lis[j][i] + 1
            m = max(lis[j+1][i+1], m)
        else:
            lis[j+1][i+1] = max(lis[j+1][i], lis[j][i+1])

temp = ''
x = len(b)
y = len(a)
for i in range(x*y):
    if lis[x][y] == 0:
        break
    if lis[x][y] == lis[x-1][y]:
        x = x-1
    elif lis[x][y] == lis[x][y-1]:
        y = y-1
    else:
        x = x-1
        y = y-1
        temp += a[y]
temp = list(temp)
temp.reverse()
print(''.join(temp))
