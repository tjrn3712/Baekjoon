import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n = int(input())
ans = [3] + [2*(i+1) for i in range(n-1)]
if n%3 == 2:
    ans[-1] += 4
print(*ans)