import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


t = int(input())
for _ in range(t):
    sh, sm, dh, dm = minput()
    tm = dh*60+dm
    print("""------+---------
 time | elapsed
------+---------""")

    ch = sh
    i = 0
    while True:
        if i==0: off=-sm
        else: off=60*i-sm

        if i!=0 and off>tm: break
        if i == 0: print(f"{ch:2d}:XX | XX") if sm == 0 else print(f"{ch:2d}:XX | XX - {sm}")
        else: print(f"{ch:2d}:XX | XX + {off}")

        ch = ch%12+1
        i+=1
