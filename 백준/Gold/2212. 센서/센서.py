import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
k = int(ipt())
sen = list(minput())
sen.sort()
dp = []
for i in range(n-1):
    dp.append(sen[i+1]-sen[i])
dp.sort()
for i in range(k-1):
    if dp:
        dp.pop()
heapq.heapify(dp)
while len(dp) > k:
    heapq.heappush(dp, heapq.heappop(dp) + heapq.heappop(dp))
print(sum(dp))
