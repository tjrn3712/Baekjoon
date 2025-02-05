import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


def kruskal(n, edges, ans):
    edges.sort()
    cnt = 0
    for i in range(n):
        if find(edges[i][1]) != find(edges[i][2]):
            union(edges[i][1], edges[i][2])
            ans += edges[i][0]
            ans += t*cnt
            cnt += 1
    return ans

def union(a, b):
    a = find(a)
    b = find(b)
    p[a] = p[b]


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


n,m,t = minput()
p = [*range(n)]
edges = []
for i in range(m):
    a,b,c = minput()
    edges.append([c,a-1,b-1])
print(kruskal(m,edges,0))