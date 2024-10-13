import sys
from collections import deque
import math
import heapq
import random
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
dp = [1]*n
l = list(minput())
for i in range(1, n):
    temp = 1
    for j in range(i):
        if l[i] > l[j]:
            temp = max(temp, dp[j] + 1)
        else:
            pass
    dp[i] = temp

print(max(dp))