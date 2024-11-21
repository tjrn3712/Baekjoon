import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
mod = 998244353
def minput(): return map(int, ipt().split())


def merge(a, b):
    return [(a[0]+b[0])//2, a[1]+b[1]]


n = int(ipt())
temp = n
ans = list(minput())
for i in range(2*n-1):
    ans[i] = [ans[i], [ans[i]]]
ans = deque(ans)
chk = []
while True:
    for i in range(n - 1):
        x, y, z = ans.popleft(), ans.popleft(), ans.popleft()
        if x[0] & 1 and y[0] & 1:
            ans.append(merge(x, y))
            if i != n - 2:
                ans.appendleft(z)
        elif y[0] & 1 and z[0] & 1:
            ans.append(merge(y, z))
            if i != n - 2:
                ans.appendleft(x)
        elif x[0] & 1 and z[0] & 1:
            ans.append(merge(x, z))
            if i != n - 2:
                ans.appendleft(y)
        elif not x[0] & 1 and not y[0] & 1:
            ans.append(merge(x, y))
            if i != n - 2:
                ans.appendleft(z)
        elif not y[0] & 1 and not z[0] & 1:
            ans.append(merge(y, z))
            if i != n - 2:
                ans.appendleft(x)
        elif not x[0] & 1 and not z[0] & 1:
            ans.append(merge(x, z))
            if i != n - 2:
                ans.appendleft(y)
    n //= 2
    if len(ans) == 1:
        break

for i in range(temp):
    print(ans[0][1][i], end=' ')
