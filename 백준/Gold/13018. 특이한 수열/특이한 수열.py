import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n, k = minput()
k = n-k
p = [str(i+2) for i in range(k-1)]
p.append('1')
for i in range(n-k):
    p.append(str(k+i+1))
if k == 0:
    print('Impossible')
    sys.exit()
print(' '.join(p))