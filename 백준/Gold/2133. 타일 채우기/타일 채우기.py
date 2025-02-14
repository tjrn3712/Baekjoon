import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


n = int(input())
dp = [0]*31
dp[0] = 1
dp[2] = 3

for i in range(4,31,2):
    dp[i] = sum(dp[:i-2])*2+dp[i-2]*dp[2]

print(0 if n&1 else dp[n])