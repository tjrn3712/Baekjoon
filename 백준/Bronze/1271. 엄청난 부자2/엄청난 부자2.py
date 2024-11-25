import sys
from collections import deque
import math
import heapq
import random
import itertools
input = sys.stdin.readline
sys.set_int_max_str_digits(1001)
INF = float('inf')
MOD = 998244353
def minput(): return map(int, input().split())


n,m=minput()
print(n//m)
print(n%m)
