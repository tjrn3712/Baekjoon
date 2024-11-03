import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n,k,m = minput()
o = []
p = []
temp = m
while n:
    o.append(n%m)
    p.append(k%m)
    n //= m
    k //= m

ans = 1
for i in range(len(o)):
    ans *= math.comb(o[i], p[i])
print(ans%m)
