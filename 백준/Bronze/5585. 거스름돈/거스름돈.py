import sys
from collections import deque
import math
import heapq
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())

n = int(ipt())
n = 1000-n

coins = 0

coins += n // 500
n %= 500
coins += n // 100
n %= 100
coins += n // 50
n %= 50
coins += n // 10
n %= 10
coins += n // 5
n %= 5
coins += n

print(coins)
