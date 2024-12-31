import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n, q = minput()
s = []
for i in range(n):
    s.append(set([*minput()][1:]))
for _ in range(q):
    line = [*minput()]
    if line[0] == 1:
        if len(s[line[1]-1]) >= len(s[line[2]-1]):
            s[line[1]-1] |= s[line[2]-1]
        else:
            s[line[2]-1] |= s[line[1]-1]
            s[line[1]-1], s[line[2]-1] = s[line[2]-1], s[line[1]-1]
        s[line[2]-1].clear()
    else:
        print(len(s[line[1]-1]))