import sys
from collections import deque
import math
import heapq
import random
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


r, c = minput()
l = []
for i in range(r):
    l.append(list(ipt().rstrip('\n')))

res = 1
for i in range(r):
    for j in range(c):
        if l[i][j] == '.':
            l[i][j] = 'D'
        elif l[i][j] == 'W':
            left = j-1
            right = j+1
            up = i-1
            down = i+1
            if left == -1:
                left = 0
            if right == c:
                right = c-1
            if up == -1:
                up = 0
            if down == r:
                down = r-1
            if l[up][j] == 'S' or l[down][j] == 'S' or l[i][left] == 'S' or l[i][right] == 'S':
                res = 0

if res:
    print(res)
    for i in range(r):
        print(''.join(l[i]))
else:
    print(res)