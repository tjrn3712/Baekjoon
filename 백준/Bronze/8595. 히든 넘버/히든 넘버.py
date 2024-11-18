import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())
mod = 10**9+7


n=int(ipt())
l = ipt()
ans = 0
temp = '0'
for i in range(n):
    if l[i].isdigit():
        temp += l[i]
    else:
        if len(temp) > 7:
            temp = '0'
        else:
            ans += int(temp)
            temp = '0'
ans += int(temp)
print(ans)

