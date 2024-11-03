import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
sys.set_int_max_str_digits(10**9)
def minput(): return map(int, ipt().split())


n = int(ipt())
stair = []
for _ in range(n):
    stair.append(int(ipt()))
if n < 3:
    print(sum(stair))
    sys.exit()
dp = [0]*n
dp[0], dp[1], dp[2] = stair[0], stair[0]+stair[1], max(stair[0]+stair[2], stair[1]+stair[2])
for i in range(3, n):
    dp[i] = max(dp[i-2]+stair[i], dp[i-3]+stair[i-1]+stair[i])
print(dp[-1])