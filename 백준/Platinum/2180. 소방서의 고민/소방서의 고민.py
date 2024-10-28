import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
l = []
for _ in range(n):
    l.append(list(minput()))
l.sort(key=lambda x: x[1]/x[0] if x[0] else x[1]*40000000001)
k = 0
for i in range(len(l)):
    k += (l[i][0]*k)%40000 + l[i][1] % 40000
    k %= 40000

print(k)