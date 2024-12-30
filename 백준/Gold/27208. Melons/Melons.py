import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
INF = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n, ll = minput()
a = []
for _ in range(n):
    a.append(int(input()))
dp = [0]*n
prefix = [0]*n
ans = [0]*n
prefix[0] = a[0]
temp = 0
cnt = 1
for i in range(1, n):
    prefix[i] = prefix[i-1]+a[i]
for i in range(n-1,-1,-1):
    l = i
    r = n-1
    while l<r-1:
        m = (l+r)//2
        if prefix[m+1]-prefix[i] <= ll: l = m
        else: r = m
    temp += a[i]
    if temp > ll:
        cnt += 1
        temp = a[i]
    dp[i] = cnt
    ans[i] = prefix[r]-prefix[i] if r == n-1 else ans[r]
temp = 0
for i in range(n):
    if temp + a[i] > ll:
        temp = 0
    temp += a[i]
for i in range(n):
    print(dp[i], ans[i-1] if i else temp)