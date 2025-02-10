import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())
sys.setrecursionlimit(10**9)


def union(a, b):
    a = find(a)
    b = find(b)
    p[a] = p[b]


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


n, q = minput()
v = [*range(n+1)]
query = []
for i in range(n-1): v[i+2] = int(input())
for i in range(n+q-1):
    line = [*minput()]
    query.append(line)
query = query[::-1]
p = [*range(n+1)]
ans = []
for line in query:
    if line[0] == 0:
        b = line[1]
        union(b, v[b])
    else:
        c, d = line[1:]
        if find(c) == find(d): ans.append('YES')
        else: ans.append('NO')
print(*ans[::-1], sep='\n')