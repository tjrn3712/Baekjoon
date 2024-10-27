import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


l = ipt().strip()
k = []
for i in range(len(l)):
    if l[i].isupper():
        k.append(l[i])
a, b, c, d = 0,0,0,0
for i in k:
    if not a:
        if i == 'U':
            a = 1
    elif not b:
        if i == 'C':
            b = 1
    elif not c:
        if i == 'P':
            c = 1
    elif not d:
        if i == 'C':
            d = 1

if d:
    print('I love UCPC')
else:
    print('I hate UCPC')