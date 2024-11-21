import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
mod = 998244353
def minput(): return map(int, ipt().split())

n, m = minput()
box = [list(minput()) for _ in range(n)]

total = 0

for i in range(1, n-1):
    for j in range(1, m-1):
        current = box[i][j]
        top = box[i-1][j]
        bottom = box[i+1][j]
        left = box[i][j-1]
        right = box[i][j+1]
        min_adj = min(top, bottom, left, right)
        covered = min(current - 1, min_adj)
        if covered > 0:
            total += covered

print(total)
