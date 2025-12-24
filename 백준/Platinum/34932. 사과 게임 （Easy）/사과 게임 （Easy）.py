import sys
from collections import deque
input = sys.stdin.readline
def minput(): return map(int, input().split())

n=int(input())
v=deque([*minput()])
if ~n&1: exit(print("Lulu"))
if min(v): exit(print("Terra"))
m=n//2

for i in range(n):
    v.rotate()
    if v[m]: continue
    l=0
    r=n-1
    ok=1
    while l<r:
        if v[l]!=v[r]:
            ok=0
            break
        l+=1
        r-=1
    if ok: exit(print("Lulu"))
print("Terra")
