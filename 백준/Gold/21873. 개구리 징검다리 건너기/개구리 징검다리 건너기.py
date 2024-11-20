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
ans = deque()
print(n*(n+2))
for i in range(2*n+1):
    if i < n:
        ans.append(i+1)
    elif i > n+1:
        ans.popleft()
    for j in range(len(ans)):
        print(2 if i&1 else 1, ans[j])
