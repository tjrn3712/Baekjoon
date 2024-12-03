import sys
from collections import deque
import math
import heapq
import random
import itertools
input = sys.stdin.readline
INF = float('inf')
MOD = 10**9+7
def minput(): return map(int, input().split())


n = int(input())
ans = [[0]*n for i in range(n)]
temp = 1
if n == 3:
    print(2, 5, 8)
    print(7, 1, 3)
    print(4, 9, 6)
    sys.exit()
if n&1:
    for i in range(1, n, 2):
        for j in range(i+1):
            ans[i-j][j] = temp
            temp += 1
    for i in range(n, -1, -2):
        for j in range(n-i+1, n):
            ans[n-j+n-i][j] = temp
            temp += 1
    for i in range(0, n, 2):
        for j in range(i+1):
            ans[i-j][j] = temp
            temp += 1
    for i in range(n-1, 1, -2):
        for j in range(n-i, n-1):
            ans[n-j+n-i-1][j+1] = temp
            temp += 1
else:
    for i in range(0, n, 2):
        for j in range(i+1):
            ans[i-j][j] = temp
            temp += 1
    for i in range(n-1, 0, -2):
        for j in range(n-i, n):
            ans[n-j+n-i-1][j] = temp
            temp += 1
    for i in range(1, n, 2):
        for j in range(i+1):
            ans[i-j][j] = temp
            temp += 1
    for i in range(n-2, 0, -2):
        for j in range(n-i, n):
            ans[n-j+n-i-1][j] = temp
            temp += 1
for i in range(n):
    print(*ans[i])
    pass
