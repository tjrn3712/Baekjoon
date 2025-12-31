import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n,m,k=minput()
arr=[int(input())for _ in range(n)]
bucket = []
last=n//1000*1000
for i in range(n//1000):
    bucket.append([0,[0]*1000,0])
    for j in range(1000):
        bucket[i][1][j]=arr[i*1000+j]
        bucket[i][0]+=arr[i*1000+j]
bucket.append([0,[0]*1000,0])
for i in range(last,n):
    bucket[-1][1][i-last]=arr[i]
    bucket[-1][0]+=arr[i]
for _ in range(m+k):
    a,b,*c=minput()
    if a==1:
        c,d=c
        b-=1
        c-=1
        if b//1000==c//1000:
            for i in range(b%1000,c%1000+1):
                bucket[b//1000][1][i]+=d
                bucket[b//1000][0]+=d
        else:
            for i in range(b//1000+1,c//1000):
                bucket[i][0]+=1000*d
                bucket[i][2]+=d
            for i in range(b%1000,1000):
                bucket[b//1000][1][i]+=d
                bucket[b//1000][0]+=d
            for i in range(c%1000+1):
                bucket[c//1000][1][i]+=d
                bucket[c//1000][0]+=d

    else:
        c=c[0]
        b-=1
        c-=1
        ans=0
        if b//1000==c//1000:
            print(sum(bucket[b//1000][1][b%1000:c%1000+1])+(c-b+1)*bucket[b//1000][2])
        else:
            for i in range(b//1000+1,c//1000):
                ans+=bucket[i][0]
            ans+=sum(bucket[b//1000][1][b%1000:])+bucket[b//1000][2]*(1000-b%1000)
            ans+=sum(bucket[c//1000][1][:c%1000+1])+bucket[c//1000][2]*(c%1000+1)
            print(ans)
