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


def dijkstra(graph, i, j, distance):
    pq = []
    distance[i][j] = dist[i][j]
    heapq.heappush(pq, (distance[i][j], i, j))
    while pq:
        dist_now, c_i, c_j = heapq.heappop(pq)
        if distance[c_i][c_j] < dist_now:
            continue
        for k in graph[c_i][c_j]:
            if dist_now + k[2] < distance[k[0]][k[1]]:
                distance[k[0]][k[1]] = dist_now + k[2]
                heapq.heappush(pq, (distance[k[0]][k[1]], k[0], k[1]))


case = 1
while True:
    n = int(input())
    if not n:
        break
    dist = [[INF]*(n) for i in range(n)]
    graph = [[[] for i in range(n)] for j in range(n)]
    for i in range(n):
        temp = [*minput()]
        for j in range(n):
            dist[i][j] = temp[j]
    for i in range(n):
        for j in range(n):
            if i:
                graph[i][j].append((i-1, j, dist[i-1][j]))
            if j:
                graph[i][j].append((i, j-1, dist[i][j-1]))
            if i<n-1:
                graph[i][j].append((i+1, j, dist[i+1][j]))
            if j<n-1:
                graph[i][j].append((i, j+1, dist[i][j+1]))
    dist2 = [[INF] * (n) for i in range(n)]
    dijkstra(graph, 0, 0, dist2)
    print('Problem', str(case)+':', dist2[n-1][n-1])
    case += 1
