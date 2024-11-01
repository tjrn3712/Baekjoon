import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
sys.set_int_max_str_digits(10**9)
def minput(): return map(int, ipt().split())


def init(start, end, index):
    if start == end:
        if arr[start] % 2:
            tree[index] = [1, 0]
        else:
            tree[index] = [0, 1]
        return
    mid = (start + end) // 2
    init(start, mid, index*2)
    init(mid+1, end, index*2+1)
    tree[index][0] = tree[index*2][0] + tree[index*2+1][0]
    tree[index][1] = tree[index*2][1] + tree[index*2+1][1]
    return

def query(start, end, index, left, right):
    if start > right or end < left:
        return [0, 0]
    if start >= left and end <= right:
        return tree[index]
    mid = (start + end) // 2
    a = query(start, mid, index*2, left, right)
    b = query(mid+1, end, index*2+1, left, right)
    return [a[0]+b[0], a[1]+b[1]]


def update(start, end, index, i, value):
    if start > i or end < i:
        return
    if start == end and start == i:
        if value % 2:
            tree[index] = [1, 0]
        else:
            tree[index] = [0, 1]
        return
    mid = (start + end) // 2
    update(start, mid, index*2, i, value)
    update(mid+1, end, index*2+1, i, value)
    tree[index][0] = tree[index * 2][0] + tree[index * 2 + 1][0]
    tree[index][1] = tree[index * 2][1] + tree[index * 2 + 1][1]
    return


n = int(ipt())
arr = list(minput())
tree = [[0, 0] for i in range(2*2**math.ceil(math.log(n, 2)))]
init(0, n-1, 1)
m = int(ipt())
for _ in range(m):
    a, b, c = minput()
    if a == 1:
        update(0, n-1, 1, b-1, c)
    elif a == 2:
        print(query(0, n - 1, 1, b - 1, c - 1)[1])
    else:
        print(query(0, n - 1, 1, b - 1, c - 1)[0])