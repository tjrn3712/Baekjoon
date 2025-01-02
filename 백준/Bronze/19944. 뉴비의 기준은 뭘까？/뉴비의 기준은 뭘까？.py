import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n, m = minput()
if m in (1,2):
    print('NEWBIE!')
elif m <= n:
    print('OLDBIE!')
else:
    print('TLE!')
