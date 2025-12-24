import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n,t=minput()
s=[*input().strip()]
#abababababab
#aabababababb
#aaababababbb
#aaaabababbbb
#aaaaababbbbb
#aaaaaabbbbbb

b=[0]
for i in range(1,n-1):
    if s[i-1]==s[i]or s[i]==s[i+1]:b.append(i)
b.append(n-1)

ans=s[:]
for i in range(len(b)-1):
    l=b[i]
    r=b[i+1]
    if l+1==r:continue

    m=(l+r)//2
    ll=min(l+t,m)
    rr=max(r-t,m+1)

    if ll>l:ans[l+1:ll+1]=s[l]*(ll-l)
    if rr<r:ans[rr:r]=s[r]*(r-rr)
    if ll<rr:ans[ll+1:rr]=['A' if j=='B' else 'B' for j in ans[ll+1:rr]]
print(''.join(ans))