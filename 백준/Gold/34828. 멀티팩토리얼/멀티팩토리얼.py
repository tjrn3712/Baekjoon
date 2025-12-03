import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

f=[[i for i in range(100001)] for k in range(301)]
for k in range(1,301):
    f[k][0]=1
    for i in range(k):
        for n in range(k+i,100001,k):
            f[k][n]=(f[k][n-k]*n)%998244353

q=int(input())
for _ in range(q):
    n,k=minput()
    ans=1
    if k>300:
        for i in range(n,0,-k):
            ans*=i
            ans%=998244353
        print(ans)
        continue
    print(f[k][n])

