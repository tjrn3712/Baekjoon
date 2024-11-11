import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
p = list(minput())
tmp = 0
for i in range(n):
    tmp ^= p[i]
if tmp:
    print('koosaga')
else:
    print('cubelover')