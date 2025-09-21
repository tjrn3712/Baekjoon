import sys, math
input = sys.stdin.readline
def minput(): return map(int, input().split())


t = int(input())
for _ in range(t):
    x = int(input())
    if x:
        ans = 1
        while x:
            ans<<=1
            x>>=1
        print(2)
        print(ans, ans+1)
    else:
        print(1)
        print(998244353)