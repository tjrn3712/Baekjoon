import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


t = int(input())
for _ in range(t):
    n=int(input())
    b=[*range(1,n+1)]
    print('?',*b,flush=True)
    
    q=[*minput()]
    c=[[0]*(n+1) for i in range(n+1)]
    for i in range(n): c[0][b[i]]=q[i]
    for i in range(2,n):
        p=[i]
        for v in range(1,n+1):
            if v!=i: p.append(v)
        print('?',*p,flush=True)
        q=[*minput()]
        a=[0]*(n+1)
        for j in range(len(p)): a[p[j]]=q[j]
        c[i]=a[:]
    cnt=dict()
    for i in range(2,n):
        for j in range(1,i):
            k=c[0][j]-c[i][j]
            if k>0: cnt[(j,i)]=cnt.get((j,i),0)+k
    for i in range(1,n):
        s=0
        for j in range(i+1,n): s+=cnt.get((i,j),0)
        k=c[0][i]-s
        if k>0: cnt[(i,n)]=cnt.get((i,n),0)+k
    M=sum(cnt.values())
    print('!',M,flush=False)
    for (i,j),k in cnt.items():
        for ___ in range(k): print(i,j,flush=False)
    sys.stdout.flush()


sys.stdout.flush()