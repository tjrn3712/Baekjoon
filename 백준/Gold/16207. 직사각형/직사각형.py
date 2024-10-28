import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())

def st(sts):
    global check
    if not sts or len(sts) == 1:
        check = False
        return 0, 0
    a1 = sts.pop()
    if a1 in sts:
        a2 = sts.pop()
    else:
        a1 -= 1
        if a1 in sts:
            a2 = sts.pop()
        else:
            return st(sts)
    return a1, a2


n = int(ipt())
stick = list(minput())

stick.sort()
check = True
s = 0
while check:
    a1, a2 = st(stick)
    b1, b2 = st(stick)
    s += a1*b1
print(s)