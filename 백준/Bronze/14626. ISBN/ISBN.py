import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())

s=input().strip()
a=0
for i in range(12):
    if s[i]=='*': continue
    j=int(s[i])
    a+=j if ~i&1 else j*3
m=int(s[-1])
if not m: m=10
w=s.find('*')
for i in range(10):
    if 10-m-(a+i if ~w&1 else a+i*3)%10==0:
        exit(print(i))
