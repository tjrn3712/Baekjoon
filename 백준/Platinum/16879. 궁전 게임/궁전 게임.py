import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


def mex(a):
    for i in range(len(a)):
        if i not in a:
            return i


n = int(ipt())
palace = []
grid = [[0 for i in range(3000)] for j in range(3000)]
for i in range(3000):
    for j in range(3000):
        grid[i][j] = ((i//3)^(j//3))*3+(i+j)%3
for _ in range(n):
    x, y = minput()
    palace.append(grid[x][y])
tmp = 0
for i in range(n):
    tmp ^= palace[i]
if tmp:
    print('koosaga')
else:
    print('cubelover')