import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n = int(input())
s = input().strip()
a = [0]*(n-1)
for i in range(n-1):
    if s[i]!=s[i+1]: a[i]=1
ans = 0
for i in range(n-2):
    if a[i] and a[i+1]: ans+=1
q = int(input())
for _ in range(q):
    query = [*minput()]
    if query[0]==1:
        l, r = query[1:]
        l-=2
        r-=1
        if -1<l<n-1:
            if l-1>=0 and a[l-1] and a[l]: ans-=1
            if l<n-2 and a[l] and a[l+1]: ans-=1
            a[l]^=1
            if l-1>=0 and a[l-1] and a[l]: ans+=1
            if l+1<n-1 and a[l] and a[l+1]: ans+=1
        if -1<r<n-1:
            if r-1>=0 and a[r-1] and a[r]: ans-=1
            if r<n-2 and a[r] and a[r+1]: ans-=1
            a[r]^=1
            if r-1>=0 and a[r-1] and a[r]: ans+=1
            if r+1<n-1 and a[r] and a[r+1]: ans+=1
    else: print(ans)
# 웨않됌???????????????모가문제지
# 아 l=0이면 l-1이 참이구나;ㅋㅋㅋ
# a[-1]zㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ졸린가