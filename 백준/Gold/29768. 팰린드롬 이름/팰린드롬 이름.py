import sys
from collections import deque
import math
import heapq
import random
import itertools
input = sys.stdin.readline
INF = float('inf')
MOD = 10**9+7
def minput(): return map(int, input().split())


n, k = minput()
ans = 'a'*(n-k)
for i in range(k):
    ans += 'abcdefghijklmnopqrstuvwxyz'[i]
print(ans)