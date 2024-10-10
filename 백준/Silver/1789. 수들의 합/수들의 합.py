import sys
from collections import deque
import math
import heapq
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


s = []
sum = 0
for i in range(150000):
    sum += i
    s.append(sum)

n = int(ipt())
left = 0
right = 150000
while abs(left - right) > 1:
    mid = (left + right) // 2
    if s[mid] > n:
        right = mid
    else:
        left = mid

print(left)