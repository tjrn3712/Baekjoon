import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


t = int(input())
for _ in range(t):
    s = input().rstrip()
    a=[[0]*26for i in range(len(s))]
    ans=0
    j=1
    for i in range(len(s)):
        if i==0:
            a[i][ord(s[i])-97]+=1
            ans+=1
            continue
        a[j][ord(s[i])-97]+=1
        if a[j-1]!=a[j]:
            j+=1
            ans+=1
    print(ans)

