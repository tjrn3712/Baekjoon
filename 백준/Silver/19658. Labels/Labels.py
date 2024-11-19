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
a = list(minput())
s = [a[0]]
for i in range(1, n-1):
    s.append(a[i]+s[-1])
d = [0]*n
d[0] = 1 - min(min(s), 0)
for i in range(1, n):
    d[i] = d[i-1]+a[i-1]
if max(d) == n and min(d) == 1:
    for i in range(n):
        print(d[i], end=' ')
else:
    print(-1)