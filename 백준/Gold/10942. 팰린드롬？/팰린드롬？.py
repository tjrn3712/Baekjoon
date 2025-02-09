import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


n = int(input())
a = [*minput()]
m = int(input())
dp = [[0 for i in range(n)] for j in range(n)]
# dp[i][j] = i ~ j까지가 팰린드롬인가?

for i in range(n):
    dp[i][i] = 1
    if i+1<n: dp[i][i+1] = 1 if a[i]==a[i+1] else 0
#for i in range(n):
#    for j in range(i+2,n): dp[i][j] = 1 if a[i]==a[j] and dp[i+1][j-1] else 0
# 왜 코드 이따구로 짰지 하수
for i in range(n-1,-1,-1):
    for j in range(n-1,i+1,-1): dp[i][j] = 1 if a[i]==a[j] and dp[i+1][j-1] else 0

for _ in range(m):
    s,e = minput()
    print(dp[s-1][e-1])