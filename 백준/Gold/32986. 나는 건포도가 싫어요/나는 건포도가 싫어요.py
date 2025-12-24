import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

x,y,z=minput()
ans=0
if min(x,y,z)<3: print(0)
elif min(x,y,z)==max(x,y,z) and x==3: print(0)
else: print((min(x,y,z)-1)//2)