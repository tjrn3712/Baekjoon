import sys
from collections import deque
import math
import heapq
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
if n%10 != 0:
    print(-1)
else:
    a=n//300
    n%=300
    b=n//60
    n%=60
    c=n//10
    n%=10
    print(a, b, c)