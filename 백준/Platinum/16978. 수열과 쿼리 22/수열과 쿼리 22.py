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
m = int(input())
seg = SegmentTree(a, lambda a,b: a+b, 0)
query1 = []
query2 = []
temp = 0
for i in range(m):
    line = [*minput()]
    if line[0] == 1:
        query1.append(line[1:])
    else:
        query2.append([line[1:], temp])
        temp += 1
query2.sort(key=lambda x:x[0])
now = 0
ans = []
for i in range(len(query2)):
    while query2[i][0][0] > now:
        seg.update_index(query1[now][0]-1, query1[now][1])
        now += 1
    ans.append([seg.query(query2[i][0][1]-1, query2[i][0][2]-1), query2[i][1]])
ans.sort(key=lambda x:x[1])
for i in ans:
    print(i[0])