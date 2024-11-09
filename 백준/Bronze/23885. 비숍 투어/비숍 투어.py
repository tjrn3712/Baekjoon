import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


n,m = minput()
s = list(minput())
e = list(minput())
if m == 1 or n == 1:
    if s == e:
        print('YES')
    else:
        print('NO')
else:
    if (s[0]+s[1]) % 2:
        if (e[0]+e[1]) % 2:
            print('YES')
        else:
            print('NO')
    else:
        if (e[0] + e[1]) % 2:
            print('NO')
        else:
            print('YES')