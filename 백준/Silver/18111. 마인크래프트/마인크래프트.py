import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n,m,b=minput()
gr=[]
for i in range(n):
    gr.append([*minput()])
g=0
ans=9982441358884841557
for h in range(256,-1,-1):
    r=0
    d=0
    for i in range(n):
        for j in range(m):
            if gr[i][j]>h:d+=gr[i][j]-h
            else:r+=h-gr[i][j]
    if r>d+b:continue
    sec=d*2+r
    if sec<ans:
        ans=sec
        g=h
print(ans,g)
