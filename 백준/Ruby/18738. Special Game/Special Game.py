import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n = int(input())
d = [*minput()]
p = [*minput()]

d.sort()
p.sort()

t=1
ans = 0
while 1:
    if not d: break
    if d[0]>p[-1]:
        if t: ans+=len(d)
        break

    x=y=-1
    tt=-998244353
    j=0
    for i in range(len(d)):
        while j<len(d) and p[j]<d[i]: j+=1
        if j==len(d): break
        if i-j>tt:
            tt=i-j
            x=i
            y=j

    if not t: ans+=1
    d.pop(x)
    p.pop(y)

    d,p=p,d
    t^=1
print(ans)