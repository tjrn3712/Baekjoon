import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


k, n = minput()
cnt = 0
for i in range(1, n+1):
    if (math.gcd(i, k) == 1 or math.gcd(i, k) == 2) and i != k:
        cnt += 1
print(cnt)