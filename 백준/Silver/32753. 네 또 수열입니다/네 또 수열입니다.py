import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
INF = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n, k = minput()
if n == 1:
    print(*[1]*k)
elif n == 2:
    if k == 1:
        print(1, 2)
    else: print(-1)
else:
    print(-1)