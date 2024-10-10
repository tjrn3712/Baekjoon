import sys
from collections import deque
import math
import heapq
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
a = list(map(str, ipt().rstrip('\n').split()))
s = []
ss = []
for i in a:
    s.append([i*10, i])
s.sort(reverse=True)
for i in s:
    ss.append(i[1])
print(int(''.join(ss)))