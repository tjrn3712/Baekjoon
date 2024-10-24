import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


t = int(ipt())
for _ in range(t):
    l = ipt().rstrip()
    if '+' in l:
        print(sum(list(map(int, l.replace('+', ' ').split()))))
    else:
        print('skipped')