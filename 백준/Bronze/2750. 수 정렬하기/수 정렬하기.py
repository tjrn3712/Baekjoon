import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


s = []
for _ in range(int(ipt())):
    heapq.heappush(s, int(ipt()))
for o in range(len(s)):
    print(heapq.heappop(s))

