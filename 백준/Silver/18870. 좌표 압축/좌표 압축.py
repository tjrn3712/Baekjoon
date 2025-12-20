import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n=int(input())
x=[*minput()]
p={}
a=sorted(x)
used=set()
y=0
for i in range(n):
    if a[i] in used: continue
    p[a[i]]=y
    used.add(a[i])
    y+=1
ans=[0]*n
for i in range(n):
    ans[i]=p[x[i]]
print(*ans)