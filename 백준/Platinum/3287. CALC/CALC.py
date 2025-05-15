import sys
input = sys.stdin.readline


s = input().strip()
n = len(s)
ans = []


def solve(l,r):
    if l==r:
        if s[l]=='A': ans.extend(["SWAP","DUP","DUP","ROT","ROT","DROP"])
        elif s[l]=='B': ans.extend(["DUP","DUP","ROT","ROT","DROP","SWAP"])
        return

    t=0
    for i in range(l+1,r):
        if s[i]=='(': t+=1
        elif s[i]==')': t-=1
        elif t==0 and s[i] in "#$":
            solve(l+1,i-1)
            solve(i+1,r-1)
            ans.extend(["ROT","ROT","DOLLAR" if s[i]=="$" else "HASH","DUP","ROT","ROT","ROT","DROP"])
            return


solve(0,n-1)
print(*ans,"DROP","DROP",sep='\n')