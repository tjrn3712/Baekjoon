import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
k = list(minput())
dp = k[:]

for i in range(1, n):
    dp[i] = max(dp[i], dp[i-1]+k[i], k[i-1]+k[i])

print(max(dp))