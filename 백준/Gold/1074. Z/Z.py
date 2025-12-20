import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n,r,c=minput()
def d(i,j,n):
    #print(n,i,j)
    if n==0:return 0
    return 4*d(i//2,j//2,n-1)+(i%2)*2+j%2
print(d(r,c,n))