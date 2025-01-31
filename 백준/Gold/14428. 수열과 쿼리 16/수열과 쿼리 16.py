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


n = int(input())
a = [*minput()]
for i in range(n):
    a[i] = [a[i], i]
m = int(input())
seg = SegmentTree(a, min, [mod<<10,mod])
for i in range(m):
    a,b,c = minput()
    if a == 1: seg.update_index(b-1,[c,b-1])
    else: print(seg.query(b-1,c-1)[1]+1)
