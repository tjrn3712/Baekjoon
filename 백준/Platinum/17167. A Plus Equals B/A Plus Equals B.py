import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

a,b=minput()
ans=0
ret=[]
while a!=b:
    if a>b:
        if ~a&1:
            a>>=1
            ans+=1
            ret.append("B+=B")
        else:
            while ~b&1:
                b>>=1
                ans+=1
                ret.append("A+=A")
            a+=b
            ans+=1
            ret.append("A+=B")
    if b>a:
        if ~b&1:
            b>>=1
            ans+=1
            ret.append("A+=A")
        else:
            while ~a&1:
                a>>=1
                ans+=1
                ret.append("B+=B")
            b+=a
            ans+=1
            ret.append("B+=A")
print(ans)
print(*ret,sep='\n')