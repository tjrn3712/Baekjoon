import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())
mod = 10**9+7

def init(start, end, index):
    if start == end:
        tree[index] = [0, arr[start]]
        return tree[index]
    mid = (start+end) // 2
    tree[index] = sorted(init(start, mid, index*2) + init(mid+1, end, index*2+1))[-2:]
    return tree[index]


def query(start, end, index, left, right):
    if start > right or end < left:
        return [0, 0]
    if start >= left and end <= right:
        return tree[index]
    mid = (start+end) // 2
    return sorted(query(start, mid, index*2, left, right) + query(mid+1, end, index*2+1, left, right))[-2:]

def update(start, end, index, i, value):
    if start > i or end < i:
        return
    if start == end:
        tree[index] = [value]
        return
    mid = (start+end) // 2
    update(start, mid, index * 2, i, value)
    update(mid + 1, end, index * 2 + 1, i, value)
    tree[index] = sorted(tree[index*2] + tree[index*2+1])[-2:]
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
        print(sum(query(0, n-1, 1, b-1, c-1)))

