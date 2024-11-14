import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n, m = minput()
nim = []
for i in range(n):
    nim.append(list(minput()))
tmp = 0
for i in range(n):
    tmp ^= sum(nim[i])
if tmp:
    print('august14')
else:
    print('ainta')