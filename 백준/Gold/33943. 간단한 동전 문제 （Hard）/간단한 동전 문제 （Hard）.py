import sys
from collections import deque
input = sys.stdin.readline
def minput(): return map(int, input().split())

n, m = minput()
if m==0: exit(print(0))
if n==0: exit(print(-1))
a = [*minput()]
p = [i for i in a if i]
q = deque()
q.append((10000,0))
coin = [0]*20001
while q:
    t, cnt = q.popleft()
    for i in p:
        if -1<t+i<20001 and not coin[t+i]:
            if t+i==m+10000: exit(print(cnt+1))
            coin[t+i] = 1
            q.append((t+i,cnt+1))
print(-1)
