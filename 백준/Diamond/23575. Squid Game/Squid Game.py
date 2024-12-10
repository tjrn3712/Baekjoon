import sys
import time
from collections import deque
import math
import heapq
import random
import itertools
input = sys.stdin.readline
INF = float('inf')
sys.set_int_max_str_digits(10**9)
MOD = 10**9+7
def minput(): return map(int, input().split())


x, y, z = minput()
water = [[x, 1], [y, 2], [z, 3]]
ans = []
cnt = 0
while water[0][0] and water[1][0] and water[2][0]:
    temp = list(bin(water[1][0] // water[0][0]))
    temp.reverse()
    cnt += len(temp)-2
    for i in range(len(temp)-2):
        if temp[i] == '1':
            water[1][0] -= water[0][0]
            water[0][0] *= 2
            ans.append((water[1][1], water[0][1]))
        else:
            water[2][0] -= water[0][0]
            water[0][0] *= 2
            ans.append((water[2][1], water[0][1]))
    water.sort()
print(cnt)
for i in ans:
    print(*i)
