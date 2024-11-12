import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n, m = minput()
ans = [[0]*m for _ in range(n)]
ans[0][0] = '10000000'
temp = 1
for i in range(n):
    if i:
        if i&1:
            ans[i][0] = str(int(ans[i-1][0]) - temp)
        else:
            ans[i][0] = str(int(ans[i-1][0]) + temp)
        temp += m
    for j in range(1, m):
        if i&1:
            if j&1:
                ans[i][j] = str(int(ans[i][j-1]) + temp)
            else:
                ans[i][j] = str(int(ans[i][j-1]) - temp)
        else:
            if j & 1:
                ans[i][j] = str(int(ans[i][j-1]) - temp)
            else:
                ans[i][j] = str(int(ans[i][j-1]) + temp)
        temp += 1
for i in range(n):
    print(' '.join(ans[i]))