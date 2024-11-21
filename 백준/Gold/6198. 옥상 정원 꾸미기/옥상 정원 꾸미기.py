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
stack = []
ans = 0
for _ in range(n):
    temp = int(ipt())
    while len(stack) and temp >= stack[-1]:
        stack.pop()
    ans += len(stack)
    stack.append(temp)
print(ans)
