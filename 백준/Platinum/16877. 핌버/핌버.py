import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


def mex(a):
    for i in range(len(a)+1):
        if i not in a:
            return i
    return len(a)+1

fib = [0,1]
for i in range(2,34):
    fib.append(fib[-1]+fib[-2])
grundy = [0]*3000001
grundy[1], grundy[2], grundy[3] = 1, 2, 3
k = [1,2,3]
for i in range(4, 3000001):
    tmp = []
    if i in fib:
        k.append(i)
    for j in range(len(k)):
        tmp.append(grundy[i-k[j]])
    grundy[i] = mex(tmp)

n = int(ipt())
p = list(minput())
t = 0
for i in range(n):
    t ^= grundy[p[i]]
if t:
    print('koosaga')
else:
    print('cubelover')