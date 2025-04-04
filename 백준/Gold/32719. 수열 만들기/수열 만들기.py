import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


n = int(input())
if n in (2, 5): exit(print(-1))
if n == 1: exit(print(1))
ans = [n,n,1]

if n%3==0: print(*(ans*(n//3)))
elif n%3==1: print(*(ans*(n//3)+[n]))
else: print(*(ans*(n//3-2)+[n,n,n,1]+[n,1,n,1]))
