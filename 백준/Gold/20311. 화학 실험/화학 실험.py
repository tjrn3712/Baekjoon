import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n, k = minput()
a = list(minput())
colors = []
for i in range(k):
    heapq.heappush(colors, (-a[i], a[i], i+1))
if colors[0][1] > math.ceil(n/2):
    print(-1)
else:
    ans = [0]*n
    j = 0
    i = 0
    now = heapq.heappop(colors)
    while j < n:
        ans[j] = str(now[2])
        i += 1
        j += 2
        if i == now[1]:
            i = 0
            if colors:
                now = heapq.heappop(colors)
    j = 1
    while j < n:
        ans[j] = str(now[2])
        i += 1
        j += 2
        if i == now[1]:
            i = 0
            if colors:
                now = heapq.heappop(colors)
    print(' '.join(ans))