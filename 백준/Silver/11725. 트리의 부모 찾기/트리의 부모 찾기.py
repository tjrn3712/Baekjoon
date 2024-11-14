import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


def bfs(graph, i, visited):
    q = deque([i])
    visited[i] = True
    while q:
        index = q.popleft()
        for node in graph[index]:
            if not visited[node]:
                visited[node] = True
                parent[node] = index
                q.append(node)


n = int(ipt())
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
parent = [0]*(n+1)
for _ in range(n-1):
    a, b = minput()
    graph[a].append(b)
    graph[b].append(a)
bfs(graph, 1, visited)
for i in range(2, n+1):
    print(parent[i])

