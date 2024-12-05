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


v = list(input().rstrip('\n').replace('C', 'U').replace('P', 'D'))
u, d = v.count('U'), v.count('D')
if u > d//2+(d&1):
    ans = 'U'
else:
    ans = ''
if d:
    ans += 'DP'
print(ans)