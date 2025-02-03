import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


a, b = minput()
n=1
while a != b:
    if ~b&1:
        b//=2
        n+=1
    elif len(str(b))-1 and str(b)[-1] == '1':
        b=int(str(b)[:-1])
        n+=1
    else:
        if a==b:
            exit(print(n))
        else:
            exit(print(-1))
print(n)