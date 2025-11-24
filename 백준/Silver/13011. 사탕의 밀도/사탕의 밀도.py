import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())
import time

n=int(input())
c=[*minput()]
w=[*minput()]
l=0
r=1000001
t1=0
t2=0
for _ in range(1000000):
    m1=(l+l+r)/3
    m2=(l+r+r)/3
    t1=0
    t2=0
    for i in range(n):
        t1+=abs(m1*c[i]-w[i])
        t2+=abs(m2*c[i]-w[i])
    if t1>t2: l=m1
    elif t1<t2: r=m2
    else:
        l=m1
        r=m2
print(t1)


