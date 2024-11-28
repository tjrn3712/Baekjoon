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


l = input().rstrip('\n')
left = 0
right = -1
chk = False
for i in range(len(l)//2):
    if l[left] != l[right]:
        chk = True
        break
    left += 1
    right -= 1
if chk:
    print(len(l))
else:
    if l.count(l[0]) == len(l):
        print(-1)
    else:
        print(len(l)-1)