import sys, heapq
input = sys.stdin.readline
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


n, m = minput()
graph = [[]for i in range(n+1)]
dist = [998244353]*(n+1)
for _ in range(m):
    a,b,c = minput()
    graph[a].append([b,c])
    graph[b].append([a,c])
s,t = minput()
dijkstra(graph, s, dist)
print(dist[t])