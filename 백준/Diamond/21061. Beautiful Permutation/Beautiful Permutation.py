import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n=int(input())
if n%4==2 or n%4==3: exit(print("NO"))
print("YES")
a=[0]*n
if n==1: exit(print(0))
if n%4==0:
    a[0]=n//2
    t=n
    for i in range(1,n//4):
        t-=1
        a[i]=t
    t-=1
    for i in range(n//4,n//2-1):
        t-=1
        a[i]=t
    t-=1
    for i in range(n//2-1,3*n//4-1):
        t-=1
        a[i]=t
    a[3*n//4-1]=3*n//4
    for i in range(3*n//4,n):
        t-=1
        a[i]=t
else:
    t=n
    for i in range(n//4):
        t-=1
        a[i]=t
    a[n//4]=n//4
    for i in range(n//4+1,n//2+1):
        t-=1
        a[i]=t
    a[n//2+1]=0
    for i in range(n//2+2,3*n//4+2):
        t-=1
        a[i]=t
    t-=1
    for i in range(3*n//4+2,n):
        t-=1
        a[i]=t
print(*a)
