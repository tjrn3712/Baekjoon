import sys, math
input = sys.stdin.readline
def minput(): return map(int,input().split())


n,p,v = minput()
if n==1: sys.exit(print(0))
ans = 9*10**18
for i in range(1, int(math.log2(n))+2):
    t = int(n**(1.0/i))
    temp = 0
    for d in range(i+1):
        temp = d
        if (t+1)**d*(t**(i-d)) >= n: break
    ans = min(ans, (t*i+temp)*p+v*i)
print(ans)
