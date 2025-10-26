import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

s = input().strip()
ans = 50000
h=0
g=0
for i in s:
    if i in 'SAD': g+=1
    if i in 'HAPPY': h+=1
if h or g:
    ans = h*100000//(h+g)
if ans%10>4: ans+=10
ans//=10
if not ans: exit(print('0.00'))
ans=str(ans)
if len(ans)==5: exit(print('100.00'))
if len(ans)==3: exit(print(ans[0]+'.'+ans[1]+ans[2]))
if len(ans)==2: exit(print('0.'+ans[0]+ans[1]))
if len(ans)==1: exit(print('0.0'+ans[0]))
print(ans[0]+ans[1]+'.'+ans[2]+ans[3])