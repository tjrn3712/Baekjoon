import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n, m = minput()
a = [*minput()]
x, y = minput()

if x==0: exit(print(m-y))
a.sort()
b = [1,n-x+1]
for i in a:
    b.append(i+1)
    b.append(i-x+1)
c = []
for i in b:
    if i>0 and i<=n-x+1:
        c.append(i)
c = sorted(set(c))

l=0
r=-1
ans = m

for i in c:
    j = i+x
    while r+1<m and a[r+1]<j: r+=1
    while l<=r and a[l]<i: l+=1
    ans = min(ans,max(0,r-l+1))
print(max(0,m-max(y,ans)))