import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


m = int(input())
a = [*minput()]

st = [[0 for i in range(m)] for j in range(31)]

st[0] = [i for i in range(1, m+1)]
st[1] = a[:]
for i in range(2, 31):
    for j in range(m):
        st[i][j] = st[i-1][st[i-1][j]-1]

q = int(input())
for i in range(q):
    n, x = minput()
    for i in range(31):
        if n&(1<<i):
            x = st[i+1][x-1]
    print(x)