import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


def bfs(graph, i, visited):
    global answer
    q = deque()
    if not visited[i]:
        answer += 1
        visited[i] = True
        for j in graph[i]:
            q.append(j)
    while q:
        temp = q.popleft()
        if not visited[temp]:
            visited[temp] = True
            for j in graph[temp]:
                q.append(j)

answer = 0
n, m = minput()
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    u, v = minput()
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, n+1):
    bfs(graph, i, visited)
print(answer)