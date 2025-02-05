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


n = int(input())
p = [*range(n)]
coord = []
edges = []
for i in range(n):
    x, y = map(float, input().split())
    coord.append([x, y])
for i, j in itertools.combinations([*range(n)], 2):
    edges.append([math.dist(coord[i], coord[j]), i, j])
print(kruskal(len(edges), edges, 0))