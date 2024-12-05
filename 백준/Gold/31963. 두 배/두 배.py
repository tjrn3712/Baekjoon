import sys
from collections import deque
import math
import heapq
import random
import itertools
input = sys.stdin.readline
INF = float('inf')
sys.set_int_max_str_digits(1000000)
MOD = 10**9+7
def minput(): return map(int, input().split())


n = int(input())
a = [*minput()]
cnt = 0
for i in range(n-1):
    if a[i] > a[i+1]:
        cnt += math.ceil(math.log(a[i] / a[i + 1], 2))
        a[i+1] *= pow(2, math.ceil(math.log(a[i]/a[i+1], 2)))
print(cnt)