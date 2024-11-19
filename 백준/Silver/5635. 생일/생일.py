import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
mod = 10**9+7
def minput(): return map(int, ipt().split())


n = int(ipt())
b = []
for _ in range(n):
    b.append(list(ipt().rstrip('\n').split()))
    b[_][1], b[_][2], b[_][3] = map(int, b[_][1:])
b.sort(key= lambda x: x[-1:0:-1])
print(b[-1][0])
print(b[0][0])
