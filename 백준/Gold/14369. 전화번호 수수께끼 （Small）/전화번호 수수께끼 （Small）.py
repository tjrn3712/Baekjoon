import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque, Counter
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


T = int(input())
for t in range(1, T+1):
    s = input().strip()
    cnt = Counter(s)
    num = [0]*10
    num[0] = cnt['Z']
    num[2] = cnt['W']
    num[4] = cnt['U']
    num[6] = cnt['X']
    num[8] = cnt['G']
    num[3] = cnt['H'] - num[8]
    num[5] = cnt['F'] - num[4]
    num[7] = cnt['S'] - num[6]
    num[1] = cnt['O'] - num[0] - num[2] - num[4]
    num[9] = cnt['I'] - num[5] - num[6] - num[8]
    res = ''.join(str(d)*num[d] for d in range(10))
    print("Case #{}: {}".format(t, res))
