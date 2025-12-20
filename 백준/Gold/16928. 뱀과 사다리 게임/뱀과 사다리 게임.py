import sys
from collections import deque
input = sys.stdin.readline
def minput(): return map(int, input().split())

n,m=minput()
lad=[0]*101
snk=[0]*101
for i in range(n):
    x,y=minput()
    lad[x]=y
for i in range(m):
    x,y=minput()
    snk[x]=y
dst=[-1]*101
q=deque([[1]])
dst[1]=0
while q:
    x=q.popleft()
    nxt=[]
    for i in x:
        for d in range(1,7):
            ni=i+d
            if ni<101:
                if lad[ni]:ni=lad[ni]
                elif snk[ni]:ni=snk[ni]
                if dst[ni]==-1:dst[ni]=dst[i]+1;nxt.append(ni)
    if dst[100]!=-1: exit(print(dst[100]))
    if not nxt: break
    q.append(nxt)
print(dst[100])
