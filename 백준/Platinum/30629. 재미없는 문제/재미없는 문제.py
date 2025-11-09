import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n,m = minput()
ans = [1]*n
if m<n:
    for i in range(n-m):
        ans[i]=0
    exit(print(*ans))
ans[0]=0
s = n//2-1
for i in range(n//2,n):
    s+=n//2
    if s>m: ans[i]=0
    else: ans[i]=n//2
if sum(ans)<m: ans[-1]=m-sum(ans)
print(*ans)