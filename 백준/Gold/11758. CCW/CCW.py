import sys
from collections import deque
import math
import heapq
sys.setrecursionlimit(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())

p1 = list(minput())
p2 = list(minput())
p3 = list(minput())

a = [p2[0] - p1[0], p2[1] - p1[1]]
b = [p3[0] - p2[0], p3[1] - p2[1]]
z = a[0]*b[1] -b[0]*a[1]
if z > 0:
    print(1)
elif z == 0:
    print(0)
else:
    print(-1)
