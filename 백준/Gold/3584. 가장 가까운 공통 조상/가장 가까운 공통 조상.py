import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


t = int(input())
for _ in range(t):
    n = int(input())
    parent = [-1]*n
    graph = []
    for i in range(n-1):
        a, b = minput()
        parent[b-1] = a-1
    a, b = minput()
    a-=1
    b-=1

    ap = [a]
    bp = [b]

    while parent[a] != -1:
        ap.append(parent[a])
        a = parent[a]
    while parent[b] != -1:
        bp.append(parent[b])
        b = parent[b]

    if len(ap) > len(bp):
        i = len(ap)-len(bp)
        j = 0
    elif len(ap) < len(bp):
        i = 0
        j = len(bp)-len(ap)
    else:
        i = 0
        j = 0

    while ap[i] != bp[j]:
        i+=1
        j+=1
    print(ap[i]+1)
