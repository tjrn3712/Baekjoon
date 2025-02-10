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


n,m=minput()
p=[*range(n)]
cnt = 0
for i in range(m):
    cnt += 1
    a,b = minput()
    if find(a)!=find(b):union(a,b)
    else:exit(print(cnt))
print(0)