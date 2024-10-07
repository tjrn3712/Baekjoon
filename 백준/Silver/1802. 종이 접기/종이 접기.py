import sys
from collections import deque
import math
import heapq
sys.setrecursionlimit(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())

def gtrei(a):
    if len(a) == 1:
        return True
    mid = len(a)//2
    for i in range(1, mid+1):
        if a[mid-i] == a[mid+i]:
            return False

    return gtrei(a[:mid])

for i in range(int(ipt())):
    a = list(ipt().rstrip('\n'))
    Y = gtrei(a)

    if Y:
        print('YES')
    else:
        print('NO')
