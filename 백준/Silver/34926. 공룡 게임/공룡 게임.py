import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n,k=minput()
s=[*input().strip()]

can=[0]*n
can[0]=1
for i in range(n-1):
    if can[i]:
        if s[i+1]=='_': can[i+1]=1
        if i+k<n and s[i+k]=='_': can[i+k]=1
if can[n-1]:
    print("YES")
else:
    print("NO")
