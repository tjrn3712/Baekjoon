import sys
from collections import deque
import math
import heapq
import random
import itertools
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())
mod = 10**9+7


n = int(ipt())
for _ in range(n):
    h, w = minput()
    bmi = (w/(h/100)**2)
    if h < 140.1:
        print(6)
    elif h < 146:
        print(5)
    elif h < 159:
        print(4)
    elif h < 161:
        if bmi >= 16 and bmi < 35:
            print(3)
        else:
            print(4)
    elif h < 204:
        if bmi >= 20 and bmi < 25:
            print(1)
        elif bmi >= 18.5 and bmi < 30:
            print(2)
        elif bmi >= 16 and bmi < 35:
            print(3)
        else:
            print(4)
    else:
        print(4)

