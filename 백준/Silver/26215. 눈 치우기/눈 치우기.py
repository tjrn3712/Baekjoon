import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
a = list(minput())
a.sort(reverse=True)
temp = sum(a)
while sum(a) != a[0]:
    a[0] -= a[1]
    temp -= a[1]
    a[1] = 0
    a.sort(reverse=True)
if temp > 1440:
    print(-1)
else:
    print(temp)