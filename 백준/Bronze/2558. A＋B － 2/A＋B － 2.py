import sys
from collections import deque
import math
import heapq
import random
import itertools
input = sys.stdin.readline
sys.set_int_max_str_digits(2001)
INF = float('inf')
MOD = 998244353
def minput(): return map(int, input().split())


a = int(input())
b = int(input())
print(a+b)