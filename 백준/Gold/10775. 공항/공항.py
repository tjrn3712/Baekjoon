import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


def union(a, b):
    a = find(a)
    b = find(b)
    p[a] = p[b]


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


g = int(input())
pl = int(input())
v = [int(input())for i in range(pl)]
p = [*range(g+1)]
for i in range(pl):
    gate = find(v[i])
    if not gate: exit(print(i))
    union(gate, gate-1)
print(g)
