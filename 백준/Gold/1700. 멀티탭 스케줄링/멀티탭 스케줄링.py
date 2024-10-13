import sys
from collections import deque
import math
import heapq
import random
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n, k = minput()
use = list(minput())
plug = []
cnt = 0
for i in range(len(use)):
    if len(plug) < n and use[i] not in plug:
        plug.append(use[i])
    elif use[i] in plug:
        pass
    else:
        ind = 0
        check = False
        for j in range(len(plug)):
            if plug[j] not in use[i:]:
                ba = plug[j]
                check = True
                break
            else:
                ind = max(ind, use[i:].index(plug[j]))
                ba = use[i:][ind]
        cnt += 1
        if check:
            plug.remove(ba)
            plug.append(use[i])
        else:
            plug.remove(ba)
            plug.append(use[i])
print(cnt)