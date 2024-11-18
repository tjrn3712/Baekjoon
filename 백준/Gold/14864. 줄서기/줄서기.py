import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())
mod = 10**9+7


n, m = minput()
ans = [i for i in range(n+1)]
for i in range(m):
    x, y = minput()
    ans[x] += 1
    ans[y] -= 1

if len(list(set(ans[1:]))) != n:
    print(-1)
    sys.exit()
for i in range(1, n+1):
    print(ans[i], end=' ')
