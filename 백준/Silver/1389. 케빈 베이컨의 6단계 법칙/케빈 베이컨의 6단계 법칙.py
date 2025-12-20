import sys
from collections import deque
input = sys.stdin.readline
def minput(): return map(int, input().split())

n,m=minput()
g=[[]for i in range(n+1)]

for i in range(m):
    a,b=minput()
    g[a].append(b)
    g[b].append(a)

an=(998244353,0)
for i in range(1,n+1):
    d=[-1]*(n+1)
    d[i]=0
    q=deque([i])
    while q:
        v=q.popleft()
        for u in g[v]:
            if d[u]==-1:
                d[u]=d[v]+1
                q.append(u)
    ans=0
    for x in range(1,n+1): ans+=d[x]if d[x]!=-1 else 998244353
    an=min(an,(ans,i))
print(an[1])