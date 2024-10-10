import sys
from collections import deque
import math
import heapq
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


k, n = minput()
a = []
for _ in range(k):
    a.append(str(ipt().rstrip('\n')))
s = []
ss = []
for i in a:
    s.append([i*10, i])
s.sort(reverse=True)
for i in s:
    ss.append(i[1])
ss.sort(key=len, reverse=True)
for _ in range(n-k):
    s.append([ss[0]*10, ss[0]])
ss.clear()
s.sort(reverse=True)
for i in s:
    ss.append(i[1])

print(int(''.join(ss)))