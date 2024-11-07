import sys
from collections import deque
import math
import heapq
import random
ipt = sys.stdin.readline
def minput(): return map(int, ipt().split())


class SegmentTree:
    # non-recursive
    # by tjrn3712(2024.11.07)
    def __init__(self, arr, merge, i):
        self.i = i
        self.N = len(arr)
        self.tree = [i for _ in range(self.N << 1)]
        self.merge = merge
        for j in range(self.N):
            self.tree[self.N+j] = arr[j]
        for j in range(self.N-1, 0, -1):
            self.tree[j] = merge(self.tree[j<<1], self.tree[j<<1|1])

    def update_index(self, index, value):
        index += self.N
        self.tree[index] = value
        while index > 1:
            self.tree[index>>1] = self.merge(self.tree[index], self.tree[index^1])
            index >>= 1

    # [left, right)
    # [left, right-1]
    def query(self, left, right):
        left += self.N
        right += self.N
        result = self.i
        while left < right:
            if left & 1:
                result = self.merge(result, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                result = self.merge(result, self.tree[right])
            left >>= 1
            right >>= 1
        return result

    def update_range(self, left, right, value):
        pass
        # studying
        # lazy propagation(non-recursive)

def merge(a, b):
    return min(a, b)


n = int(ipt())
a = list(minput())
arr = []
for i in range(n):
    arr.append([a[i], i])
seg = SegmentTree(arr, merge, [10**9+7,0])
m = int(ipt())
for _ in range(m):
    k = list(minput())
    if k[0] == 1:
        seg.update_index(k[1]-1, [k[2], k[1]-1])
    else:
        print(seg.query(0, n)[1]+1)