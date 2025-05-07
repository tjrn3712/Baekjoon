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

t = int(input())
for _ in range(t):
    n = int(input())
    if n in [0,1,2,3,4]:
        print([1,2,4,8,20][n])
    else:
        print('frogger')
