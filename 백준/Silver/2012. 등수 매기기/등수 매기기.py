import sys
from collections import deque
import math
import heapq
import random
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
d = []
for i in range(n):
    d.append(int(ipt()))

d.sort()
sum = 0
for i in range(n):
    sum += abs(d[i] - i - 1)
print(sum)