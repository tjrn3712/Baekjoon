i=input
p=print
p('?',n:=int(i()),1)
p('!',c:=int(i()),n^c and(p('?',n-c,1)or i())or 1)