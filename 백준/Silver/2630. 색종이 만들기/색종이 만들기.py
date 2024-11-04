import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
sys.setrecursionlimit(10**9)
def minput(): return map(int, ipt().split())


def div(left, right, top, bottom):
    global a
    global b
    zero = False
    one = False
    for i in range(bottom - top):
        if 0 in paper[top+i][left:right+1]:
            zero = True
        if 1 in paper[top+i][left:right+1]:
            one = True
    chk = zero & one
    if zero and not one:
        a += 1
    if one and not zero:
        b += 1
    if not chk:
        return
    mid = (left+right) // 2
    mid2 = (top+bottom) // 2
    div(left, mid, top, mid2)
    div(mid+1, right, top, mid2)
    div(left, mid, mid2, bottom)
    div(mid+1, right, mid2, bottom)
    return




n = int(ipt())
paper = []
a = 0
b = 0
for _ in range(n):
    paper.append(list(minput()))
div(0, n-1, 0, n)
print(a)
print(b)
