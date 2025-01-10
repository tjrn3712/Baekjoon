import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


t = int(input())
for _ in range(t):
    x, r, c = minput()
    ans = 0
    if max(r, c) < x:
        ans = 0
    elif (r*c)%x:
        ans = 0
    elif min(r, c) < (x+1)//2:
        ans = 0
    elif x == 1:
        ans = 1
    elif x == 2:
        if (r*c)&1:
            ans = 0
        else:
            ans = 1
    elif x == 3:
        if (r*c)%3:
            ans = 0
        elif min(r, c) == 1:
            ans = 0
        else:
            ans = 1
    elif x == 4:
        if (r*c)%4:
            ans = 0
        elif min(r, c) <= 2:
            ans = 0
        elif max(r, c) < 4:
            ans = 0
        else:
            ans = 1
    elif x == 5:
        if (r*c)%5:
            ans = 0
        elif min(r, c) <= 2:
            ans = 0
        elif min(r, c) == 3 and max(r, c) == 5:
            ans = 0
        else:
            ans = 1
    elif x == 6:
        if (r*c)%6:
            ans = 0
        elif min(r, c) <= 3:
            ans = 0
        elif max(r, c) < 6:
            ans = 0
        else:
            ans = 1
    else:
        ans = 0
    if not ans: print("Case #", _+1, ": RICHARD", sep='')
    else: print("Case #", _+1, ": GABRIEL", sep='')