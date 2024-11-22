import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
mod = 998244353
def minput(): return map(int, ipt().split())


t = int(ipt())
q = deque()
for _ in range(t):
    op = ipt().split()
    if op[0] == 'push':
        q.append(int(op[1]))
    elif op[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif op[0] == 'size':
        print(len(q))
    elif op[0] == 'front':
        if q: print(q[0])
        else: print(-1)
    elif op[0] == 'back':
        if q:print(q[-1])
        else:print(-1)
    elif op[0] == 'empty':
        print(int(not bool(q)))
