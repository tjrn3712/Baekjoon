import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())
mod = 10**9+7


n = int(ipt())
if n == 1:
    print('B')
else:
    print('A')