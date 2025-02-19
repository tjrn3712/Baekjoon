import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = min(init(start, mid, index*2), init(mid+1, end, index*2+1))
    return tree[index]

def query(start, end, index, left, right):
    if start > right or end < left:
        return 10**9+7
    if start >= left and end <= right:
        return tree[index]
    mid = (start + end) // 2
    return min(query(start, mid, index*2, left, right), query(mid+1, end, index*2+1, left, right))

def update(start, end, index, i, value):
    if start > i or end < i:
        return
    if start == end and start == i:
        tree[index] = value
        return
    mid = (start + end) // 2
    update(start, mid, index*2, i, value)
    update(mid+1, end, index*2+1, i, value)
    tree[index] = min(tree[index*2], tree[index*2+1])
    return


n = int(ipt())
tree = [0]*2*2**math.ceil(math.log(n, 2))
arr = list(minput())
init(0, n-1, 1)
m = int(ipt())
for _ in range(m):
    a, b, c = minput()
    if a == 1:
        update(0, n-1, 1, b-1, c)
    elif a == 2:
        print(query(0, n-1, 1, b-1, c-1))