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


v, e = minput()
k = int(input())
graph = [[]] + [[] for i in range(v)]
dist = [INF]*(v+1)
for _ in range(e):
    u, vv, w = minput()
    graph[u].append((vv, w))
dijkstra(graph, k, dist)
for i in range(1, v+1):
    if dist[i] == INF: print('INF')
    else: print(dist[i])
