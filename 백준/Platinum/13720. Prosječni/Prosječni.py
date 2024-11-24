import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
mod = 998244353
def minput(): return map(int, ipt().split())


n = int(ipt())
if n == 2:
    exit(print(-1))
if n&1:
    temp = 0
    for i in range(n):
        print(*range(temp+1, temp+n+1))
        temp += n
else:
    temp = 0
    ans = [i if i <= n//2 else i+n-1 for i in range(2, n-1)]
    ans = [n] + ans + [n-1, 2*n-1]
    for j in ans:
        print(*[ii + 10000*j for ii in ans])

