import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())
mod = 10**9+7


while True:
    a = list(map(int, ipt().rstrip('\n').replace(' ','')))
    if sum(a) == 0:
        break
    for i in range(0,16,2):
        a[i]*=2
        if a[i]>9:
            a[i]-=9
    s = str(sum(a))
    if s[-1] == '0':
        print('Yes')
    else:
        print('No')

