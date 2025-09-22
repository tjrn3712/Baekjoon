import sys
from collections import deque
input = sys.stdin.readline
def minput(): return map(int, input().split())


dd = [(0,1),(0,-1),(1,0),(-1,0)]
n,m,r,c = minput()
room = []
shop = []
for i in range(r):
    a, b ,p = minput()
    room.append([p,a,b])
for i in range(c):
    cc, d = minput()
    shop.append([cc,d])

grid = [[0]*(m+1) for i in range(n+1)]
visited = [[0]*(m+1) for i in range(n+1)]
q = deque()
for i in range(c):
    q.append(shop[i]+[0])

while q:
    a = []
    while q:
        a.append(q.popleft())

    for i,j,k in a:
        if i>n or i<0 or j>m or j<0: continue
        if visited[i][j]: continue
        grid[i][j] = k
        visited[i][j] = 1
        for x,y in dd:
            q.append([i+x,j+y,k+1])


ans = 9982441358884841557
for k,i,j in room:
    ans = min(ans, grid[i][j]*k)
print(ans)
