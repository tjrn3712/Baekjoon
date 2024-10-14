import sys
from collections import deque
import math
import heapq
import random
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
cards = list(minput())
cards.sort()
if len(cards) == 1:
    print(0)
    sys.exit()
s = 0
while len(cards) != 1:
    a = cards.pop()
    b = cards.pop()
    temp = a + b
    s += temp
    cards.append(max(a, b))
print(s)