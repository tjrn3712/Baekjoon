a = ord('A')
for i in 'QWERTYUIOPASDFGHJKLXCVBNM':
    o = ord(i)
    for x,y in [(1,12), (2,8), (3,10), (4,9)]:
        print(i+chr(a+(o-a+x)%25)+chr(a+(o-a+y)%25))