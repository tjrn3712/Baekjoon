import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

def union(a, b):
    a = find(a)
    b = find(b)
    p[a] = p[b]


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def kruskal(n, adj, ans):
    adj.sort()
    for i in range(n):
        if not adj[i][3] and find(adj[i][1]) != find(adj[i][2]):
            adj[i][3] = now
            union(adj[i][1], adj[i][2])
            ans += adj[i][0]
    return ans


n, m, k = minput()
adj = []
for i in range(m):
    a, b, c = minput()
    adj.append([-c, a, b, 0, i+1])
for now in range(1, k+1):
    p = [*range(n+1)]
    kruskal(m, adj, 0)
adj.sort(key=lambda x:x[4])
for i in range(m):
    print(adj[i][3])
