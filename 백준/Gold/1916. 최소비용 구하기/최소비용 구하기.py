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


n = int(input())
m = int(input())
dist = [INF]*(n+1)
graph = [[] for i in range(n+1)]
for _ in range(m):
    u, v, d = minput()
    graph[u].append((v, d))
start, end = minput()
dijkstra(graph, start, dist)
print(dist[end])
