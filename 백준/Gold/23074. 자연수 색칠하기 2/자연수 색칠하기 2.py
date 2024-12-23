import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
INF = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n = int(input())
ans = [1]*n
temp = 1
for i in range(3, n):
    if i&1:
        temp += 1
    ans[i] = temp
print(max(ans))
print(*ans)
