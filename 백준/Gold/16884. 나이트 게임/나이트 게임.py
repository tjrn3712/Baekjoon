import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
sys.setrecursionlimit(10**9)
def minput(): return map(int, ipt().split())


t = int(ipt())
for _ in range(t):
    n = int(ipt())
    if n%2:
        print('koosaga')
    else:
        print('cubelover')