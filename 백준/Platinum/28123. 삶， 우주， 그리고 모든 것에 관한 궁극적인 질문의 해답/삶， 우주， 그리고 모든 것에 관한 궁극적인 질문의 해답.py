import sys
from collections import deque
import math
import heapq
import random
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n, k, x = minput()
l = [0, 0, 1, 1, 2, 2, 2, 2, 3, 3]
i = n - l[x]
result = i-3*k+3
if x == 4 or x == 8 or x == 9:
    result += 1
print(result)