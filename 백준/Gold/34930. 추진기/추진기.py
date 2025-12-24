import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

t=int(input())
for _ in range(t):
    l,r=minput()
    m=max(l,(r+1)//2)
    ans=[m]
    k=0
    for i in range(r,l-1,-1):
        if i==m: continue
        ans.append(-i if ~k&1 else i)
        k+=1
    print(*ans)