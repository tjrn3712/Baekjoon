import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
a = list(map(list, ipt().split()))
for i in range(n):
    a[i].reverse()
    for j in range(len(a[i])):
        if a[i][j] == '6':
            a[i][j] = '9'
        elif a[i][j] == '9':
            a[i][j] = '6'
a.sort(key=lambda x: [len(x), ''.join(x)*7])
a.append(a[-1][:])
a.sort(key=lambda x: [''.join(x)*7, ''.join(x)])
for i in range(n+1):
    a[i].reverse()
    for j in range(len(a[i])):
        if a[i][j] == '6':
            a[i][j] = '9'
        elif a[i][j] == '9':
            a[i][j] = '6'
    a[i] = ''.join(a[i])
print(''.join(a))