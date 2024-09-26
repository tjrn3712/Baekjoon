import sys
from collections import deque
import math

n = int(sys.stdin.readline())
stack = []
temp = []

for i in range(n):
    temp.append(int(sys.stdin.readline()))

result = []
no = False
a, b = 0, 1
for j in range(2*n):
    if b <= temp[a]:
        stack.append(b)
        result.append('+')
        b += 1
    else:
        if stack[-1] == temp[a]:
            stack.pop()
            result.append('-')
        else:
            no = True
            break
        a += 1

if no:
    print('NO')
else:
    print('\n'.join(result))

