i=input
p=print
t=int
n=t(i())
p('?',n,1)
c=t(i())
if c==n:exit(p('!',c,1))
p('?',n-c,1)
r=t(i())
p('!',c,r)