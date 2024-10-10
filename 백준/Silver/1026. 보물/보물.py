import sys
from collections import deque
import math
import heapq
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
a = list(minput())
b = list(minput())
s = []
b.sort()
while a:
    a.sort(key=lambda x: x * b[-1], reverse=True)
    s.append(a[-1]*b[-1])
    a.pop()
    b.pop()

print(sum(s))