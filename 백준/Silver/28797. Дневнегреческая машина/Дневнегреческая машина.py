import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
mod = 10**9+7
def minput(): return map(int, ipt().split())


a = float(ipt())
if a <= 1:
    print(100*a)
else:
    print(100+100*(a-1)/3)
