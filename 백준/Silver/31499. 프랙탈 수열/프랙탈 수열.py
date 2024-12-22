import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
INF = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n, m = minput()
print(math.factorial(n)%m)