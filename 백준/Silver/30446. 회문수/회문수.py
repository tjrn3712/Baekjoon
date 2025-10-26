import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n = int(input())
s = str(n)
ans = 0
for i in range(1, len(s)):
    ans+=9*(10**((i+1)//2-1))
m = int(s[:(len(s)+1)//2])
t = str(m)
p = int(t+(t[:-1][::-1]if len(s)&1 else t[::-1]))
ans+=max(0,m-10**((len(s)+1)//2-1)+(p<=n))
print(ans)