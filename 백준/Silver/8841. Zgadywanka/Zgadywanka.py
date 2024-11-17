import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())
mod = 10**9+7


z = int(ipt())
for _ in range(z):
    n, k = minput()
    print(math.ceil(math.log(n+1, k+1)))