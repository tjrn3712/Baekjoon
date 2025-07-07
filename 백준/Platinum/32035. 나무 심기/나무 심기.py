import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


ans = [['.']*200 for i in range(200)]
def fill(r1,c1,r2,c2):
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            ans[i][j] = 'O'


a,b = minput()
if b&1: exit(print('NO'))
if b==0:
    if a in (2,3,5,6,9): exit(print('NO'))
    if a==1:
        ans[0][0] = 'O'
    elif a==4:
        fill(0,0,1,1)
    elif a==8:
        fill(0,0,2,2)
        ans[1][1] = '.'
    elif a==12:
        fill(0,0,3,3)
        ans[1][1] = '.'
        ans[1][2] = '.'
        ans[2][1] = '.'
        ans[2][2] = '.'
    else:
        if a%3==0:
            fill(0, 0, 3, 3)
            ans[1][1] = '.'
            ans[1][2] = '.'
            ans[2][1] = '.'
            ans[2][2] = '.'
            i=3
            a-=12
        elif a%3==1:
            fill(0, 0, 1, 1)
            i=1
            a-=4
        else:
            fill(0, 0, 2, 2)
            ans[1][1] = '.'
            i=2
            a-=8
        while a!=0:
            a-=3
            fill(i,i,i+1,i+1)
            i+=1
else:
    p = b//2+1
    fill(1,0,1,a+p-1)
    for i in range(p-2):
        if ~i&1:
            ans[0][i+1]='O'
        else:
            ans[2][i+1]='O'
print('YES')
print(200,200)
for i in range(200):
    print(*ans[i],sep='')
