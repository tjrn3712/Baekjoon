import sys
from collections import deque
import math
import heapq
import random
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n, k = minput()
p = [str(i+2) for i in range(k-1)]
p.append('1')
for i in range(n-k):
    p.append(str(k+i+1))
if k == 0:
    print(-1)
    sys.exit()
print(' '.join(p))
