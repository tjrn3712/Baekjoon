import sys
from collections import deque
import math
import heapq
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


m = []
n = int(ipt())
for _ in range(n):
    a, b = minput()
    m.append([a, b])
m.sort(key=lambda x : (x[1],x[0]))
m = deque(m)
answer = [m[0]]
now = 0
end = m[0][1]
m.popleft()
while m:
    if m[0][0] < end:
        m.popleft()
    else:
        answer.append(m[0])
        end = m[0][1]
        m.popleft()

print(len(answer))