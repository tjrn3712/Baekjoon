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
l = ipt().rstrip('\n')
if l == 'Whiteking':
    a = 'Whiteking'
    b = 'Blackking'
else:
    a = 'Blackking'
    b = 'Whiteking'
tmp = 0
for i in range(n):
    p[i] -= 2
    tmp ^= p[i]
if tmp:
    print(a)
else:
    print(b)