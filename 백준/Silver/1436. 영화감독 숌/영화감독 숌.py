import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n = int(input())
temp = 0
for i in range(10**9):
    if '666' in str(i):
        temp += 1
    if temp == n:
        exit(print(i))