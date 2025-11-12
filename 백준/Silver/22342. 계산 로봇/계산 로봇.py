import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

m,n=minput()
grid=[list(map(int,list(input().strip())))for i in range(m)]
a = [0]*m
ans =0
for j in range(n):
    b = [0]*m
    for i in range(m):
        ans = max(ans,a[i])
        b[i]=a[i]+grid[i][j]
    if j==n-1:break
    c = [-998244353]*m
    for i in range(m):
        c[i]=max(c[i],a[i])
        if i>0:c[i-1]=max(c[i-1],a[i])
        if i+1<m:c[i+1]=max(c[i+1],a[i])
    for i in range(m):
        c[i]=max(c[i],b[i])
        if i>0:c[i-1]=max(c[i-1],b[i])
        if i+1<m:c[i+1]=max(c[i+1],b[i])
    a=c[:]
print(ans)