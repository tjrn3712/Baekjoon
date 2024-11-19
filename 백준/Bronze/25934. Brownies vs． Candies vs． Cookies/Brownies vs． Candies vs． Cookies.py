import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
mod = 10**9+7
def minput(): return map(int, ipt().split())


n = int(ipt())
for _ in range(n):
    s, b = minput()
    m = int(ipt())
    print('Practice #' + str(_ + 1) + ':', s, b)
    for _ in range(m):
        temp = int(ipt())
        while b <= temp:
            b *= 2
        b -= temp
        print(temp, b)
    if _ != n-1:
        print()