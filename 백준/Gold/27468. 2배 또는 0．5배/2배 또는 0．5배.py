import sys
from collections import deque
import math
import heapq
import random
import itertools
input = sys.stdin.readline
INF = float('inf')
MOD = 998244353
def minput(): return map(int, input().split())


n = int(input())
if n&1:
    ans = [3, 1, 2] + [*range(4, n+1)]
    for i in range(2, (n-1)//2 + 1):
        if i&1:
            ans[2*i], ans[2*i-1] = ans[2*i-1], ans[2*i]
else:
    ans = [*range(1, n+1)]
    for i in range((n-1)//2 + 1):
        if not i&1:
            ans[2*i], ans[2*i+1] = ans[2*i+1], ans[2*i]

print('YES')
print(*ans)