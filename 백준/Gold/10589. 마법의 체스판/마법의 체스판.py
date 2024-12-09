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


n, m = minput()
print(n//2+m//2)
for i in range(n//2):
    print(2*i+2,1,2*i+2,m)
for i in range(m//2):
    print(1,2*i+2,n,2*i+2)
