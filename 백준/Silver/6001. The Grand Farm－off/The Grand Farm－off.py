import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
mod = 998244353
def minput(): return map(int, ipt().split())


N, a, b, c, d, e, f, g, h, M = list(minput())
cows = []
a_d = a % d
b_d = b % d
c_d = c % d
e_h = e % h
f_h = f % h
g_h = g % h

for i in range(3 * N):
    i5_d = pow(i, 5, d)
    W_i = (a_d * i5_d + b_d * pow(i, 2, d) + c_d) % d
    i5_h = pow(i, 5, h)
    U_i = (e_h * i5_h + f_h * pow(i, 3, h) + g_h) % h
    cows.append((-U_i, W_i))

cows.sort()
total_weight = 0
for j in range(N):
    total_weight += cows[j][1]
    if total_weight >= M:
        total_weight %= M
print(total_weight % M)
