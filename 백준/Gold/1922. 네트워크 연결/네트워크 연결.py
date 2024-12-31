import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


def union(a, b):
    a = find(a)
    b = find(b)
    p[a] = p[b]


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def kruskal(n, edges, ans):
    edges.sort()
    for i in range(n):
        if find(edges[i][1]) != find(edges[i][2]):
            union(edges[i][1], edges[i][2])
            ans += edges[i][0]
    return ans


n = int(input())
m = int(input())
e = []
for i in range(m):
    a, b, c = minput()
    a -= 1
    b -= 1
    e.append([c, a, b])
p = [i for i in range(n)]
print(kruskal(m, e, 0))