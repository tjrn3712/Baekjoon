import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline
def minput(): return map(int, input().split())


n = int(input())
if n == 1: exit(print(0))
a = [*minput()]
m = max(a)
f = m
heapify(a)
ans = 998244353998244353

while a[0] <= f:
    temp = heappop(a)
    ans = min(ans, abs(m-temp))
    temp <<= 1
    m = max(m, temp)
    heappush(a, temp)
ans = min(ans, m-a[0])
print(ans)
