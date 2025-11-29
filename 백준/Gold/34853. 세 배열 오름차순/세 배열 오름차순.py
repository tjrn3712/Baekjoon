import sys
input = sys.stdin.readline
from bisect import bisect_right as bi
def minput(): return map(int, input().split())

n,q=minput()
k=[[]]+[sorted([*minput()][1:])for _ in range(n)]
#print(*k)
for _ in range(q):
    a,b,c,j=minput()
    A=k[a]
    B=k[b]
    C=k[c]
    #print(A)
    l=0
    r=1010101010
    while l<r:
        m=(l+r)//2
        if (bi(A,m)+bi(B,m)+bi(C,m))>=j:r=m
        else:l=m+1
    print(l)


