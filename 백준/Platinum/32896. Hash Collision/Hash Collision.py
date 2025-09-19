i=lambda:int(input())
p=print
n=i()
p('?',n,1)
c=i()
if c^n:p('?',n-c,1);p('!',c,i())
p('!',c,1)