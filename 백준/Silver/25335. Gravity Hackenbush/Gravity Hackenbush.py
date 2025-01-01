import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n, m = minput()
for i in range(n):
    input()
r = 0
g = 0
b = 0
for i in range(m):
    c = input().split()[2]

    if c == 'R':
        r += 1
    elif c == 'G':
        g += 1
    elif c == 'B':
        b += 1

if g&1:
    if r >= b:
        print('jhnah917')
    else:
        print('jhnan917')
else:
    if r>b:
        print('jhnah917')
    else:
        print('jhnan917')