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
inp = list(minput())
stack = []
ans = [-1]*n
for i in range(n):
    j = 1
    while len(stack) and inp[i] > stack[-1]:
        while ans[i-j] != -1:
            j += 1
        ans[i-j] = inp[i]
        stack.pop()
        j += 1
    stack.append(inp[i])
print(*ans)
