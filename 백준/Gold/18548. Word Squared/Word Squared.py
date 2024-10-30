import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
a = deque(ipt().rstrip('\n').split())
print(2*n-1)
for _ in range(2*n-1):
    temp = list(a) + list(a)[:n-1]
    print(' '.join(temp))
    a.rotate(-1)