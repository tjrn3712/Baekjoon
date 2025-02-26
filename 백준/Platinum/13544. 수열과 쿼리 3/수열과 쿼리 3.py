import sys
from bisect import bisect_right
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

    def query_count(self, left, right, k):
        left += self.N
        right += self.N+1
        res = 0
        while left < right:
            if left & 1:
                res += len(self.tree[left])-bisect_right(self.tree[left], k)
                left += 1
            if right & 1:
                right -= 1
                res += len(self.tree[right])-bisect_right(self.tree[right], k)
            left //= 2
            right //= 2
        return res


def merge(a, b):
    la= len(a)
    lb = len(b)
    i=j=0
    ret = []
    while i < la and j < lb:
        if a[i] < b[j]:
            ret.append(a[i])
            i+=1
        else:
            ret.append(b[j])
            j+=1
    if i == la: ret+=b[j:]
    if j == lb: ret+=a[i:]
    return ret


n = int(input())
a = [*minput()]
for i in range(n): a[i] = [a[i]]
seg = SegmentTree(a, merge, [])
m = int(input())
ans = 0
for _ in range(m):
    a, b, c = minput()
    i, j, k = a^ans, b^ans, c^ans
    ans = seg.query_count(i-1,j-1,k)
    print(ans)
