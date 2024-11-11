import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
c = []
for _ in range(n):
    c.append(list(minput()))
cc = c[:]
cc.sort(key=lambda x: x[0]+x[1])
c.sort(key=lambda x: x[0]-x[1])
print(max(abs(c[-1][0]-c[0][0])+abs(c[-1][1]-c[0][1]), abs(cc[-1][0]-cc[0][0])+abs(cc[-1][1]-cc[0][1])))