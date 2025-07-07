import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


n = int(input())
nodes = []
for i in range(n):
    a,h = minput()
    nodes.append((a,h,i))

if sum(1 for _,h,_ in nodes if h==1)!=1: exit(print(-1))

nodes.sort(key=lambda x: x[0])
h = [x[1] for x in nodes]
idx = [x[2] for x in nodes]
l = [-1]*n
r = [-1]*n
stk = []
for i in range(n):
    last = -1
    while stk and h[stk[-1]]>h[i]: last = stk.pop()
    if stk: r[stk[-1]] = i
    if last != -1: l[i] = last
    stk.append(i)

root = stk[0]
depth = [0]*n
stk = [(root,1)]
while stk:
    u, d = stk.pop()
    depth[u] = d
    if r[u]!=-1: stk.append((r[u],d+1))
    if l[u]!=-1: stk.append((l[u],d+1))

for i in range(n):
    if depth[i]!=h[i]: exit(print(-1))

ansl = [-1]*n
ansr = [-1]*n
for i in range(n):
    temp = idx[i]
    if l[i]!=-1: ansl[temp] = idx[l[i]]+1
    if r[i]!=-1: ansr[temp] = idx[r[i]]+1

for i in range(n): print(ansl[i],ansr[i])
