import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())
MINF = -10**18


def seg_merge(l, r):
    total = l[0] + r[0]
    prefix = max(l[1], l[0] + r[1])
    suffix = max(r[2], r[0] + l[2])
    best = max(l[3], r[3], l[2] + r[1])
    return (total, prefix, suffix, best)

class SegmentTree:
    def __init__(self, arr, merge, i):
        self.i = i
        self.N = len(arr)
        self.tree = [i for _ in range(self.N << 1)]
        self.merge = merge
        for j in range(self.N):
            self.tree[self.N+j] = arr[j]
        for j in range(self.N-1, 0, -1):
            self.tree[j] = merge(self.tree[j<<1], self.tree[j<<1|1])

    def query(self, left, right):
        left += self.N
        right += self.N+1
        res_left = self.i
        res_right = self.i
        while left < right:
            if left & 1:
                res_left = self.merge(res_left, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                res_right = self.merge(self.tree[right], res_right)
            left //= 2
            right //= 2
        return self.merge(res_left, res_right)


n = int(input())
a = [*minput()]
seg_arr = [(x, x, x, x) for x in a]
seg = SegmentTree(seg_arr, seg_merge, (0, MINF, MINF, MINF))
m = int(input())
for _ in range(m):
    l, r = minput()
    l -= 1; r -= 1
    print(seg.query(l, r)[3])
