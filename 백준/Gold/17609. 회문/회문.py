import sys
from collections import deque
import math
import heapq
sys.setrecursionlimit(10**9)
sys.set_int_max_str_digits(10**9)
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


for _ in range(int(ipt())):
    result = 0
    e = True
    left = 0
    a = ipt().rstrip('\n')
    right = len(a)-1
    while left < right:
        if a[left] == a[right]:
            left +=1
            right -=1
        elif a[left+1] == a[right] and e:
            e = False
            left += 1
        elif a[left] == a[right-1] and e:
            e = False
            right -=1
        else:
            left += 1
            right -= 1
            result = 2
    if result != 2 and not e:
        result = 1
    result1 = 0
    e1 = True
    left1 = 0
    right1 = len(a)-1
    while left1 <= right1:
        if a[left1] == a[right1]:
            left1 +=1
            right1 -=1
        elif a[left1] == a[right1-1] and e1:
            e1 = False
            right1 -=1
        elif a[left1+1] == a[right1] and e1:
            e1 = False
            left1 += 1
        else:
            left1 += 1
            right1 -= 1
            result1 = 2
    if result1 != 2 and not e1:
        result1 = 1
    print(min(result, result1))