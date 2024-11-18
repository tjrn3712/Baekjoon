import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())
mod = 10**9+7


a, b, c, d, e = minput()
if sum([a,b,c,d]) >= 4*e:
    print(0)
else:
    print(4*e-sum([a,b,c,d]))

