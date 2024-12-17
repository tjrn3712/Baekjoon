import sys, time, math, heapq, random, itertools
from collections import deque
input = sys.stdin.readline
INF = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


x,y,c = minput()
d = math.sqrt(x*x+y*y)
print(int(d//c + int(d%c != 0)) + int(d%c != 0 and c > d))