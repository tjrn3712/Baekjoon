import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
def minput(): return map(int, input().split())


def bipartite_matching(adjacent, graph1, graph2, a, visited):
    visited[a] = True
    for b in adjacent[a]:
        if graph2[b] == -1 or not visited[graph2[b]] and bipartite_matching(adjacent, graph1, graph2, graph2[b], visited):
            graph1[a] = b
            graph2[b] = a
            return True
    return False


n, m = minput()
adj = [[] for i in range(n+1)]
for i in range(1, m+1):
    a, b = minput()
    adj[a].append(b)
ans = 0
A = [-1]*(n+1)
B = [-1]*(n+1)
for i in range(1, n+1):
    visited = [False]*(n+1)
    if bipartite_matching(adj, A, B, i, visited): ans += 1
print(ans)