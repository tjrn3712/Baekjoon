import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


t = int(ipt())
for _ in range(t):
    n, m = minput()
    air = []
    for _ in range(m):
        air.append(list(minput()))
    print(n-1)