import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n,m,s=minput()
a=[*minput()]
b=[*minput()]
sub=[]
for i in range(n):
    sub.append([a[i],b[i],i+1])

sub.sort(key=lambda x:x[1]/x[0], reverse=True)
ans=[]
#print(*sub)
for i in range(n):
    ans.append([min(m,s,sub[i][0]),sub[i][2]])
    #print(s, min(m, s, sub[i][0]))
    s-=min(m,s,sub[i][0])
ans.sort(key=lambda x:x[1])
aa=[]
for i in range(n):
    aa.append(ans[i][0])
print(*aa)
