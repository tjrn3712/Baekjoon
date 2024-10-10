import sys
from collections import deque
import math
import heapq
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


l = ipt().rstrip('\n').split('-')
for i in range(len(l)):
    l[i] = sum(list(map(int, l[i].split('+'))))

for i in range(len(l)):
    l[i] = int(l[i])

total = l[0]
for i in l[1:]:
    total -= i
print(total)
