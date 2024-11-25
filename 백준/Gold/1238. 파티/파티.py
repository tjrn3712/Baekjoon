import sys
from collections import deque
import math
import heapq
import random
import itertools
input = sys.stdin.readline
INF = float('inf')
MOD = 998244353
def minput(): return map(int, input().split())


def dijkstra(graph, i, distance):
    pq = []
    distance[i] = 0
    heapq.heappush(pq, (distance[i], i))
    while pq:
        dist_now, current = heapq.heappop(pq)
        if distance[current] < dist_now:
            continue
        for j in graph[current]:
            if dist_now + j[1] < distance[j[0]]:
                distance[j[0]] = dist_now + j[1]
                heapq.heappush(pq, (distance[j[0]], j[0]))


n, m, x = minput()
graph = [[] for i in range(n+1)]
for _ in range(m):
    u, v, d = minput()
    graph[u].append((v, d))
dists = [[INF] * (n+1) for i in range(n+1)]
for i in range(1, n+1):
    dijkstra(graph, i, dists[i])
ans = 0
for i in range(1, n+1):
    ans = max(ans, dists[i][x] + dists[x][i])
print(ans)
