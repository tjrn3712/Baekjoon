import sys
input = sys.stdin.readline
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
        res_left = self.i
        res_right = self.i
        while left < right:
            if left & 1:
                res_left = self.merge(res_left, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                res_right = self.merge(self.tree[right], res_right)
            left >>= 1
            right >>= 1
        return self.merge(res_left, res_right)


n, m = minput()
a = [*minput()]
seg = SegmentTree(a, max, 0)


ans = []
for i in range(m-1, n-m+1):
    ans.append(seg.query(i-(m-1), i+(m-1)))
print(*ans)
