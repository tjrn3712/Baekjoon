import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


n = int(input())
if not n%4 and (not n%400 or n%100):
    print(30)
else:
    print(29)