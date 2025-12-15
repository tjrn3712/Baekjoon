import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

np1C=[0]*202020
dp=[[0]*5050for i in range(5050)]
while True:
    try:
        n,x,y,q=minput()
        A=B=C=0
        query = []
        for _ in range(q):
            a,b=minput()
            query.append([a,b])
            A=max(A,a)
            B=max(B,b)
            C=max(C,a+b)
        D=max(A,B,C)

        np1C[0]=1
        for k in range(1,D+10):
            if k>n+1:
                np1C[k]=0
                continue
            np1C[k]=np1C[k-1]*(n-k+2)*pow(k,-1,998244353)%998244353

        if x==y:
            if x==0:
                for a,b in query:
                    print(int(a+b==n))
            else:
                for a,b in query:
                    if n<a+b:
                        print(0)
                    else:
                        print(pow(x,n-a-b,998244353)*np1C[a+b+1]%998244353)
            continue
        t=pow(x-y,-1,998244353)
        for a in range(A+1):
            for b in range(B+1):
                dp[a][b]=(((dp[a][b-1]if b else 0)-(dp[a-1][b]if a else 0)-(np1C[b]*pow(y,n+1-b,998244353)%998244353if a==0and b<n else 0)+(np1C[a]*pow(x,n+1-a,998244353)%998244353if b==0and a<n else 0))%998244353*t)%998244353

        for a,b in query:
            print(dp[a][b])
    except:
        break