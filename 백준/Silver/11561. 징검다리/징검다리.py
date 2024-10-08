import sys
from collections import deque
import math
import heapq
sys.setrecursionlimit(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())

s = []
for i in range(int(ipt())):
    s.append(int(ipt()))
for i in s:
    n = 1
    m = 2 * 10 ** 8
    while True:
        mid = (n+m) // 2
        an = mid*(mid+1) //2
        if i < an:
            m = mid
        elif i > an:
            n = mid
        else:
            result = mid
            break
        if n == m or m-1 == n:
            result = n
            break
    print(result)