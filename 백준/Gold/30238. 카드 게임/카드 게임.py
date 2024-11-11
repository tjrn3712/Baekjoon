import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


t = int(ipt())
for _ in range(t):
    n = int(ipt())
    a = list(minput())
    chk = False
    s = [0]*(n+1)
    for i in range(n-1,-1,-1):
        s[i] = s[i+1] + max(0, a[i])
    score = 0
    for i in range(n):
        if i % 2:
            score = max(score, s[i+1])
        else:
            score = max(score, a[i]+s[i+1])
    print(score)
