import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

n,t=minput()
z=input().strip()
a=[]
r=s=p=0
j=0
b=[]
for i in range(n):
    if z[i]=="R": r=1;b.append("R")
    if z[i]=="S": s=1;b.append("S")
    if z[i]=="P": p=1;b.append("P")
    if all([r,s,p]):
        a.append(b[:-1]);r=s=p=0;
        b=[]
        if z[i]=="R": r=1;b.append("R")
        if z[i]=="S": s=1;b.append("S")
        if z[i]=="P": p=1;b.append("P")
a.append(b[:])
ans=[]
for i in a:
    k=0
    b=['']*len(i)
    for x in range(3):
        if "RSP"[(x+2)%3] not in i:
            for j in range(len(i)):
                if i[j]=="RSP"[(x+1)%3]:
                    b[max(k,j-t)]="RSP"[(x+1)%3]
                    k+=1
            for j in range(len(i)):
                if not b[j]: b[j]="RSP"[x]
    #print(b)
    ans.append(''.join(b))
#print(a)
for i in ans:
    print(i,end='')


