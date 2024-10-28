import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
l = []
for _ in range(n):
    l.append(list(minput())+[_+1])
check = True
while check:
    check = False
    for i in range(n-1):
        if l[i][0]*l[i+1][1] > l[i+1][0]*l[i][1]:
            l[i], l[i+1] = l[i+1], l[i]
            check = True
k = []
for i in range(n):
    k.append(str(l[i][2]))

print(' '.join(k))