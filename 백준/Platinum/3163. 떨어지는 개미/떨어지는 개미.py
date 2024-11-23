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
for _ in range(t):
    n, l, k = minput()
    ants = [0]*n
    fall = [0]*n
    for i in range(n):
        ants[i] = list(minput())
        ants[i][0] = l-ants[i][0] if ants[i][1] > 0 else ants[i][0]
    fall = ants[:]
    fall.sort()
    chk = []
    for i in range(n):
        if fall[i][1] < 0:
            chk.append(-1)
        else:
            chk.append(1)
        if i:
            if fall[i][0] == fall[i-1][0]:
                chk.pop()
                chk.pop()
                chk.append(0)
    left = 0
    right = -1
    ans = []
    for i in range(len(chk)):
        if chk[i] < 0:
            ans.append(ants[left][1])
            left += 1
        elif chk[i] > 0:
            ans.append(ants[right][1])
            right -= 1
        else:
            ans += sorted([ants[left][1], ants[right][1]])
            left += 1
            right -= 1
    print(ans[k-1])

