import sys
from collections import deque
import math
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


expos = set()
s = list(range(2, 1000001))
n, m = minput()
for i in s:
    a = i ** 2
    if a not in expos:
        expos.add(a)

expos = list(expos)
expos.sort()
cnt = [1] * (m-n+1)
for i in expos:
    t = n // i
    if n % i != 0:
        t += 1
    if i > m:
        break
    a = t * i
    while a <= m:
        cnt[a - n - 1] = 0
        a += i


print(sum(cnt))
