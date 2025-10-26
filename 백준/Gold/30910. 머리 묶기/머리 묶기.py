import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

for _ in range(int(input())):
    n = int(input())
    a = [*minput()]
    if n==1 and 3 in a:
        print(-1)
        continue
    if 3 not in a:
        print(0)
        continue
    t = 0
    for i in a:
        t^=i

    if t!=3:
        print(1)
        continue
    if all(i==3 for i in a) and n&1:
        print(3)
        continue

    l = a.index(3)
    r = n-a[::-1].index(3)-1
    x = 0
    for i in range(l,r+1):
        x^=a[i]
    print(1 if x!=3 or any(a[:l]) or any(a[r+1:])else 2)