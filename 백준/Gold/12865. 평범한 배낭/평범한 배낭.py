import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


n, k = minput()
a = []
for _ in range(n):
    w,v = minput()
    a.append([w,v])
dp = [[0]*n for i in range(k+1)]
for i in range(1, k+1):
    if a[0][0] <= i:
        dp[i][0] = a[0][1]
for i in range(1, k+1):
    for j in range(1, n):
        if a[j][0] > i: dp[i][j] = dp[i][j-1]
        else: dp[i][j] = max(dp[i][j-1], a[j][1] + dp[i-a[j][0]][j-1])
print(dp[k][n-1])