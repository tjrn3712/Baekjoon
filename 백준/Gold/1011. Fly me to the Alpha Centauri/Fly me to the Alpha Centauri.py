import sys, time, math, heapq, random, itertools
from collections import deque
input = sys.stdin.readline
INF = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


t = int(input())
for _ in range(t):
    x, y = minput()
    d = y-x
    if d == 1:
        print(1)
    elif d == 2:
        print(2)
    else:
        rootd = math.floor(math.sqrt(d))
        if d <= rootd**2 + rootd:
            print(2*math.ceil(math.sqrt(d))-2) if not math.sqrt(d).is_integer() else print(2*math.ceil(math.sqrt(d))-1)
        else:
            print(2*math.ceil(math.sqrt(d))-1)
