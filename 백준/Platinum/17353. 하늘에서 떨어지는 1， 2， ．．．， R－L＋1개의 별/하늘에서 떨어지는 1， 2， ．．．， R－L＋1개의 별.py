import sys, time, math, heapq, random, itertools, operator, io, os, bisect
from collections import deque
input = sys.stdin.readline
inf = float('inf')
mod = 998244353
def minput(): return map(int, input().split())


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

    # [left, right]
    def query(self, left, right):
        left += self.N
        right += self.N+1
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


def merge(a, b):
    return a+b

n = int(input())
a = [*minput()]
arr1 = [0]*(n+1)
arr2 = [0]*(n+1)
seg1 = SegmentTree(arr1, merge, 0)
seg2 = SegmentTree(arr2, merge, 0)

q = int(input())
for _ in range(q):
    query = [*minput()]
    if query[0] == 1:
        seg1.update_index(query[1]-1, seg1.tree[seg1.N+query[1]-1]+1)
        seg1.update_index(query[2], seg1.tree[seg1.N+query[2]]-1)
        seg2.update_index(query[1]-1, seg2.tree[seg2.N+query[1]-1]+1-query[1])
        seg2.update_index(query[2], seg2.tree[seg2.N+query[2]]-1+query[1])
    else:
        print(seg1.query(0, query[1]-1)*query[1] + seg2.query(0, query[1]-1) + a[query[1]-1])
