import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())

def seg_init1(start,end,index):
    if start == end:
        tree1[index] = arr[start]
        return tree1[index]
    mid = (start+end) //2
    tree1[index] = max(seg_init1(start, mid, index * 2), seg_init1(mid + 1, end, index * 2 + 1))
    return tree1[index]
def seg_update1(start,end,index,ind_update,value):
    if ind_update < start or ind_update > end:
        return tree1[index]
    if start == end:
        tree1[index] = value
        return tree1[index]
    mid = (start + end) // 2
    tree1[index] = max(seg_update1(start, mid, index * 2, ind_update, value),
                      seg_update1(mid + 1, end, index * 2 + 1, ind_update, value))
    return tree1[index]
def seg_prefix1(start,end,index,left,right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree1[index]
    mid = (start+end) //2
    return max(seg_prefix1(start, mid, index * 2, left, right), seg_prefix1(mid + 1, end, index * 2 + 1, left, right))
def seg_init2(start,end,index):
    if start == end:
        tree2[index] = arr[start]
        return tree2[index]
    mid = (start+end) //2
    tree2[index] = min(seg_init2(start, mid, index * 2), seg_init2(mid + 1, end, index * 2 + 1))
    return tree2[index]
def seg_update2(start,end,index,ind_update,value):
    if ind_update < start or ind_update > end:
        return tree2[index]
    if start == end:
        tree2[index] = value
        return tree2[index]
    mid = (start + end) // 2
    tree2[index] = min(seg_update2(start, mid, index * 2, ind_update, value),
                      seg_update2(mid + 1, end, index * 2 + 1, ind_update, value))
    return tree2[index]
def seg_prefix2(start,end,index,left,right):
    if left > end or right < start:
        return 10**9+7
    if left <= start and right >= end:
        return tree2[index]
    mid = (start+end) //2
    return min(seg_prefix2(start, mid, index * 2, left, right), seg_prefix2(mid + 1, end, index * 2 + 1, left, right))


arr = []
n, m = minput()
for _ in range(n):
    arr.append(int(ipt()))
tree1 = [0] * 2 * 2 ** math.ceil(math.log(n, 2))
tree2 = [0] * 2 * 2 ** math.ceil(math.log(n, 2))
seg_init1(0, n - 1, 1)
seg_init2(0, n - 1, 1)
for _ in range(m):
    a, b = minput()
    print(seg_prefix2(0, n-1, 1, a-1, b-1), seg_prefix1(0, n - 1, 1, a - 1, b - 1))
