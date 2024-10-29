import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())

def seg_init(start,end,index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start+end) //2
    tree[index] = seg_init(start, mid, index*2) + seg_init(mid+1, end, index*2+1)
    return tree[index]
def seg_update(start,end,index,ind_update,value):
    if ind_update < start or ind_update > end:
        return tree[index]
    if start == end:
        tree[index] = value
        return tree[index]
    mid = (start + end) // 2
    tree[index] = seg_update(start, mid, index * 2, ind_update, value) + seg_update(mid + 1, end, index * 2 + 1, ind_update, value)
    return tree[index]
def seg_prefix(start,end,index,left,right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[index]
    mid = (start+end) //2
    return seg_prefix(start, mid, index*2, left, right)+seg_prefix(mid+1, end, index*2+1, left, right)


arr = []
n, m, k = minput()
for _ in range(n):
    arr.append(int(ipt()))
tree = [0]*2*2**math.ceil(math.log(n, 2))
seg_init(0,n-1,1)
for _ in range(m+k):
    a, b, c = minput()
    if a == 1:
        seg_update(0,n-1,1,b-1,c)
    elif a == 2:
        print(seg_prefix(0,n-1,1,b-1,c-1))
