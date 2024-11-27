import sys
from collections import deque
import math
import heapq
import random
import itertools
input = sys.stdin.readline
INF = float('inf')
MOD = 998244353
def minput(): return map(int, input().split())


n = int(input())
t = [*minput()]
a = t[:]
left = 0
right = n-1
for i in range(n):
    if a[i] != i+1:
        left = i
        break
for i in range(n-1, -1, -1):
    if a[i] != i+1:
        right = i
        break
qwer, asdf = left+1, a.index(left+1)+1
#print(left+1, a.index(left+1)+1)
#print(a.index(right+1)+1, right+1)
a = a[:left]+a[left:a.index(left+1)+1][::-1]+a[a.index(left+1)+1:]
left = 0
for i in range(n):
    if a[i] != i+1:
        left = i
        break
if a[:left]+a[left:a.index(left+1)+1][::-1]+a[a.index(left+1)+1:] == sorted(a):
    print(qwer, asdf)
    print(left+1, a.index(left+1)+1)
else:
    a = t[:]
    right = n-1
    for i in range(n-1, -1, -1):
        if a[i] != i+1:
            right = i
            break
    print(a.index(right+1)+1, right+1)
    a = a[:a.index(right+1)]+a[a.index(right+1):right+1][::-1]+a[right+1:]
    right = n-1
    for i in range(n):
        if a[i] != i+1:
            left = i
            break
    print(left+1, a.index(left+1)+1)