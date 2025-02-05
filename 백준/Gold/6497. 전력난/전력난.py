import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


def kruskal(n, edges, ans):
    edges.sort()
    for i in range(n):
        if find(edges[i][1]) != find(edges[i][2]):
            union(edges[i][1], edges[i][2])
        else:
            ans += edges[i][0]
    return ans

def union(a, b):
    a = find(a)
    b = find(b)
    p[a] = p[b]


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


while True:
    m, n = minput()
    edges = []
    if not m*n:
        break
    p = [*range(m)]
    for i in range(n):
        x, y, z = minput()
        edges.append([z,x,y])
    ans = kruskal(n, edges, 0)
    print(ans)
