import sys
from collections import deque
import math
import heapq
import random
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n, k = minput()
if n == k:
    k -= 1

xp = list(minput())
xp.sort(reverse=True)
ans = 0
s = []
sm = 0
for i in xp:
    sm += i
    s.append(sm)
print(sum(s[-k-1:-1]))