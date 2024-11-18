import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())
mod = 10**9+7


n = int(ipt())
ans = deque([5, 7, 2, 4, 6])
for i in range(9, n+1):
    if i&1:
        ans.appendleft(i)
    else:
        ans.append(i)
ans = deque(map(str, list(ans)))
ans.appendleft('3')
ans.appendleft('1')
ans.append('8')
for i in range(n):
    print(' '.join(ans))
    ans.rotate()