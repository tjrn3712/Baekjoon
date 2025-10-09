for i in'QWERTYUIOPASDFGHJKLXCVBNM':
 for x,y in[(1,12),(2,8),(3,10),(4,9)]:print(i+chr(65+((o:=ord(i))-65+x)%25)+chr(65+(o-65+y)%25))