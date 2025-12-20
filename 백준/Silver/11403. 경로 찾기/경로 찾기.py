import sys
from collections import deque
input = sys.stdin.readline
def minput(): return map(int, input().split())

n=int(input())
g=[[*minput()]for i in range(n)]
visited=[[0]*n for i in range(n)]
for i in range(n):
    q=deque([i])
    while q:
        x=q.popleft()
        for j in range(n):
            if not visited[i][j]and g[x][j]:
                q.append(j)
                visited[i][j]=1
for i in visited:print(*i)

