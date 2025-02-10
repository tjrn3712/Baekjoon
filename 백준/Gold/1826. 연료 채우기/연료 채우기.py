import sys
from heapq import heappop, heappush
input = sys.stdin.readline
def minput(): return map(int, input().split())


n = int(input())
j = [[*minput()]for i in range(n)]
l, p = minput()
pq = []
j.sort()
ans = 0

now = 0
while p<l:
    while now<n and p>=j[now][0]:
        heappush(pq, -j[now][1])
        now += 1

    if not pq: exit(print(-1))

    p -= heappop(pq)
    ans += 1
print(ans)