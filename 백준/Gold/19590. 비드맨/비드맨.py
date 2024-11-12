import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
marbles = []
for _ in range(n):
    marbles.append(int(ipt()))
m = max(marbles)
s = sum(marbles)
if n == 1:
    print(marbles[0])
else:
    if m >= s - m:
        print(2*m-s)
    else:
        if s&1:
            print(1)
        else:
            print(0)