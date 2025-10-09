for i in range(25):
 for x,y in[(1,12),(2,8),(3,10),(4,9)]:print(chr(i+65)+chr(65+(i+x)%25)+chr(65+(i+y)%25))