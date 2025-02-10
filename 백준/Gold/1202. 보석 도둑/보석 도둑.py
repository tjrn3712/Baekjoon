import sys
from heapq import heappush, heappop
from collections import deque
input = sys.stdin.readline
def minput(): return map(int, input().split())


n, k = minput()
jew = [[*minput()]for i in range(n)]
bac = [int(input())for i in range(k)]
jew.sort()
bac.sort()
jew = deque(jew)
pq = []
now = 0
ans = 0

while True:
    if now == k: break
    for i in range(len(jew)):
        jewel = jew.popleft()
        if jewel[0] > bac[now]:
            jew.appendleft(jewel)
            break
        heappush(pq, -jewel[1])
    now += 1
    if pq: ans += -heappop(pq)
    else: continue
print(ans)