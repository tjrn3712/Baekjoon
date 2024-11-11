import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


def mex(l):
    for i in range(max(l)+2):
        if i not in l:
            return i


m = [0] * 1001
m[0], m[1], m[2] = 0, 0, 1
for i in range(3, 1001):
    now = []
    for j in range(i//2+1):
        now.append(m[j]^m[i-2-j])
    m[i] = mex(now)
n = int(ipt())

if m[n]:
    print(1)
else:
    print(2)