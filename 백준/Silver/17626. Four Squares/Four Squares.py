import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n=int(input())
dp=[0]*(n+1)
i=1
while i**2<=n:
    dp[i**2]=1
    i+=1
for i in range(1,n+1):
    if dp[i]:continue
    j=1
    while j**2<=i:
        # dp[i]:=i를만드는데필요한최소수개수
        # dp[i]=min(dp[제곱수]+dp[i-제곱수],dp[i])
        if dp[i]:dp[i]=min(dp[i],dp[j*j]+dp[i-j*j])
        else: dp[i]=dp[j*j]+dp[i-j*j]
        j+=1
print(dp[n])
