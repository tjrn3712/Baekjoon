import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


p = [i for i in range(100)]
def find(a):
    if p[a] != a:
     p[a] = find(p[a])
    return p[a]
def union(a,b):
    a = find(a)
    b = find(b)
    p[a] = p[b]


n, m = minput()
k, *a = minput()
if not k: exit(print(m))

q = min(a)
for i in a:
    union(q, i)

qu = []
for i in range(m):
    qu.append([*minput()])
    for j in qu[i][1:]:
        for k in qu[i][1:]:
            union(k, j)
ans = 0
for i in range(m):
    f = True
    for j in qu[i][1:]:
        if find(q)==find(j):
            f = False
    if f:
        ans+=1
print(ans)

