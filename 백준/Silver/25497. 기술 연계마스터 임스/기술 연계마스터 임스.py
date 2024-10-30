import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n = int(ipt())
l = input()
ans = 0
s = []
ll = []
for i in l:
    if i.isdigit():
        if i == 0:
            continue
        ans += 1
    elif i == 'S':
        s.append(1)
    elif i == 'L':
        ll.append(1)
    elif i == 'K':
        if s:
            s.pop()
            ans += 1
        else:
            break
    elif i == 'R':
        if ll:
            ll.pop()
            ans += 1
        else:
            break
print(ans)