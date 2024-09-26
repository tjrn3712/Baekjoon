import sys
from collections import deque
import math
ipt = sys.stdin.readline

n, m = map(int, ipt().rstrip('\n').split())
result = []
hear = dict()
for i in range(n):
    hear[ipt().rstrip('\n')] = 0

for i in range(m):
    a = ipt().rstrip('\n')
    if a in hear:
        result.append(a)

print(len(result))
result.sort()
for i in result:
    print(i)