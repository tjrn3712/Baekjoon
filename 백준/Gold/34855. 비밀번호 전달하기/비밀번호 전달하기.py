import sys
input = sys.stdin.readline
import random
def minput(): return map(int, input().split())

t=int(input())
if t&1:
    a=[*minput()]
    for i in range(6):
        a[i]-=1
    b=[[0]*6for _ in range(6)]
    c=[[0]*6for _ in range(6)]
    for i in range(6):
        for j in range(6):
            b[i][j]=(a[i]>>j)&1
    for i in range(6):
        for j in range(6):
            c[i][j]=b[(i+j)%6][j]^1
    d=[0]*6
    for i in range(6):
        for j in range(6):
            d[i]|=c[i][j]<<j
        d[i]+=1
    print(*d)

else:
    a=[*minput()]
    for i in range(6):
        a[i]-=1
    b=[[0]*6for _ in range(6)]
    c=[[0]*6for _ in range(6)]
    for i in range(6):
        for j in range(6):
            b[i][j]=(a[i]>>j)&1
    for i in range(6):
        for j in range(6):
            c[i][j]=b[(i-j)%6][j]^1
    d=[0]*6
    for i in range(6):
        for j in range(6):
            d[i]|=c[i][j]<<j
        d[i]+=1
    print(*d)