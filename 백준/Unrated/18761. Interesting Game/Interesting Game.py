import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

t = int(input())
for _ in range(t):
    n, A, B = minput()
    a = [0]+sorted([*minput()], reverse=True)

    if B==n:
        print(a[1]+A)
        continue

    dp = [0]*((n-1)//B+1)
    ps = [0]*(n+1)
    for i in range(1,n+1): ps[i]=ps[i-1]+a[i]
    l=1
    for r in range(1,n+1,B):
        while a[l]*(r-l+1)-(ps[r]-ps[l-1])>A*(((l-1)//B)+1): l+=1
        if l==r: dp[0]=max(a[r]+A*(((r-1)//B)+1),dp[0])
        else:
            i=(r-1)//B-(((l-1)//B)+1)
            if 0<=i<=(n-1)//B:
                sz=r-l+1
                q,rm=divmod(A*((l-1)//B+1)+ps[r]-ps[l-1],sz)
                dp[i]=max(dp[i],q*(sz-((B-l%B)%B+1))+max(rm-((B-l%B)%B+1),0)+A)

    a[0]=a[1]+A+1
    aa = A
    ps2 =[0]*(n+1)
    i=n
    while i>0:
        mn=min(a[i-1]-a[i],aa//(n-i+1))
        a[i]+=mn
        ps2[i]=mn
        aa-=mn*(n-i+1)

        if a[i-1]>a[i]:
            j=i
            while aa:
                a[j]+=1
                aa-=1
                j+=1
            i+=1
            while i<=n:
                a[i]+=ps2[i-1]
                ps2[i]+=ps2[i-1]
                i+=1
            break
        i-=1

    for i in range(1,n-B+1): a[i]=a[i+B]
    for i in range(n-B+1,n+1): a[i]=0

    ps = [0]*(n+1)
    for i in range(1,n+1): ps[i]=ps[i-1]+a[i]
    l=1
    for r in range(1,n+1,B):
        while a[l]*(r-l+1)-(ps[r]-ps[l-1])>A*(((l-1)//B)+1): l+=1
        if l==r: dp[0]=max(a[r]+A*(((r-1)//B)+1),dp[0])
        else:
            i=(r-1)//B-(((l-1)//B)+1)
            if 0<=i<=(n-1)//B:
                sz=r-l+1
                q,rm=divmod(A*((l-1)//B+1)+ps[r]-ps[l-1],sz)
                dp[i]=max(dp[i],q*(sz-((B-l%B)%B+1))+max(rm-((B-l%B)%B+1),0)+A)
    for i in range((n-1)//B,0,-1):
        dp[i]=max(dp[i],(A-1)//B*min(n-B,i*B+1)+A)
        qq,rr=divmod(dp[i],i*B+1)
        dp[i-1]=max(dp[i-1],qq*((i-1)*B+1)+max(0,rr-B)+A)
    print(dp[0])
