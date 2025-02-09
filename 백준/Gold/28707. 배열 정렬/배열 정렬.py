import sys
input = sys.stdin.readline
def minput(): return map(int,input().split())
import heapq
from collections import defaultdict


def dijkstra(graph, i, distance):
    pq = []
    distance[i] = 0
    heapq.heappush(pq, (distance[i], i))
    while pq:
        dist_now, current = heapq.heappop(pq)
        if distance[current] < dist_now: continue
        if current == b: continue
        for l,r,c in graph:
            nxt = current[:l-1]+current[r-1]+current[l:r-1]+current[l-1]+current[r:]
            if nxt in dist and dist_now + c >= distance[nxt]: continue
            distance[nxt] = dist_now + c
            heapq.heappush(pq, (distance[nxt], nxt))


n = int(input())
tmp = [*minput()]
a = ''.join(str(i-1) for i in tmp)
b = ''.join(sorted(a))
m = int(input())
cmd = [[*minput()] for i in range(m)]
dist = dict()
dist[a] = 0

dijkstra(cmd, a, dist)
print(dist[b] if b in dist else -1)