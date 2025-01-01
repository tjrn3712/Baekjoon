import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n = int(input())
a = 0
b = 0
e = 0
for i in range(n):
    p = [*minput()]
    e += b*p[0]+a*p[1]
    a += p[0]
    b += p[1]
print(e)