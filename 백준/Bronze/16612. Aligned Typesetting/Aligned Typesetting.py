import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())
mod = 10**9+7


n, l = minput()
temp = 0
for _ in range(n):
    temp += len(ipt().rstrip('\n'))
if n == 1:
    if l != temp:
        print('No')
    else:
        print('Yes')
elif (l - temp) > 0 and not (l- temp)% (n-1):
    print('Yes')
else:
    print('No')