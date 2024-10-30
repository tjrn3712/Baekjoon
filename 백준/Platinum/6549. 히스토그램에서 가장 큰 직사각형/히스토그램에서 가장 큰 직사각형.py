import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


def div(start, end):
    if start == end:
        return arr[start]
    mid = (start + end) // 2
    left = mid
    right = mid
    temp = 0
    h = arr[mid]
    while True:
        if left == start and right == end:
            break
        elif left == start:
            right += 1
            h = min(h, arr[right])
            temp = max(temp, h*(right-left+1))
        elif right == end:
            left -= 1
            h = min(h, arr[left])
            temp = max(temp, h * (right - left+1))
        else:
            if arr[right+1] > arr[left-1]:
                right += 1
                h = min(h, arr[right])
                temp = max(temp, h * (right - left+1))
            else:
                left -= 1
                h = min(h, arr[left])
                temp = max(temp, h * (right - left+1))

    area = max(div(start, mid), div(mid+1, end), temp)
    return area

while True:
    k = list(minput())
    if k == [0]:
        break
    n = k[0]
    arr = k[1:]
    print(div(0, n-1))