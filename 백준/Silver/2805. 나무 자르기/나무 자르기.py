import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n,m=minput()
a=[*minput()]
l=-1
r=9982441358884841557

while l<r:
    mid=(l+r+1)//2
    s=0
    for i in a:
        s+=max(0,i-mid)
    if s>=m: l=mid
    else: r=mid-1
print(l)