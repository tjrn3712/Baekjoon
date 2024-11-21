import sys
from collections import deque
import math
import heapq
import random
import itertools
input = sys.stdin.readline
mod = 998244353
def minput(): return map(int, input().split())


n, p = minput()
guitar = [[] for i in range(7)]
cnt = 0
for _ in range(n):
    x, y = minput()
    while guitar[x] and y < guitar[x][-1]:
        guitar[x].pop()
        cnt += 1
    if guitar[x] and guitar[x][-1] == y:
        pass
    else:
        if len(guitar[x]) == p:
            guitar[x].pop()
            cnt += 1
        guitar[x].append(y)
        cnt += 1
print(cnt)