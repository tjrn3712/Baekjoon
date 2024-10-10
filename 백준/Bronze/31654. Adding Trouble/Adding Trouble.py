import sys
from collections import deque
import math
import heapq
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())

a, b, c = minput()
if a+b==c:
    print('correct!')
else:
    print('wrong!')