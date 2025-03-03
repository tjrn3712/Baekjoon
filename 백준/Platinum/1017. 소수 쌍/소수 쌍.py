import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def minput(): return map(int, input().split())


def bipartite_matching(adjacent, graph1, graph2, a, visited):
    visited[a] = True
    for b in adjacent[a]:
        if graph2[b] == -1 or not visited[graph2[b]] and bipartite_matching(adjacent, graph1, graph2, graph2[b], visited):
            graph1[a] = b
            graph2[b] = a
            return True
    return False


prime = [True]*2001
prime[0] = prime[1] = False
for i in range(2001):
    if prime[i]:
        mul = 2
        while i*mul<2001:
            prime[i*mul] = False
            mul += 1
n = int(input())
a = [*minput()]
odd = []
even = []
for i in range(n):
    if a[i]&1: odd.append(a[i])
    else: even.append(a[i])
adj = [[]for i in range(1001)]
for i in range(len(odd)):
    for j in range(len(even)):
        if prime[odd[i]+even[j]]: adj[odd[i]].append(even[j])
ans = []
for _ in range(1,n):
    if not prime[a[0]+a[_]]: continue
    cnt = 1
    A = [-1]*1001
    B = [-1]*1001
    adja = []
    for i in range(1001):
        adja.append(adj[i][:])
    if a[0]&1:
        adja[a[0]] = []
        for i in range(1001):
            if a[_] in adja[i]:
                del adja[i][adja[i].index(a[_])]
    else:
        adja[a[_]] = []
        for i in range(1001):
            if a[0] in adja[i]:
                del adja[i][adja[i].index(a[0])]
    for i in range(1001):
        visited = [False]*1001
        if bipartite_matching(adja, A, B, i, visited): cnt += 1
    if cnt == n//2:
        ans.append(a[_])

if ans: print(*sorted(ans))
else: print(-1)
