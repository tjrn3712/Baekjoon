import sys
input = sys.stdin.readline
def minput(): return map(int,input())


n = int(input())
s = list(input().rstrip())
mod1, mod2 = 10**9+7, 998244353
b = 257
f = False

o = 1
x = n
ans = 0
while o<=x:
    f = False
    mid = (o+x)//2
    t1 = set()
    t2 = set()
    hash1 = 0
    hash2 = 0
    tmp1 = 1
    tmp2 = 1
    for i in range(mid):
        hash1 += ord(s[i])*tmp1
        hash2 += ord(s[i])*tmp2
        hash1 %= mod1
        hash2 %= mod2
        tmp1 *= b
        tmp2 *= b
        tmp1 %= mod1
        tmp2 %= mod2
    t1.add(hash1)
    t2.add(hash2)

    for i in range(mid, n):
        hash1 -= ord(s[i-mid])
        hash1 *= pow(b, mod1-2, mod1)
        hash1 %= mod1
        hash1 += ord(s[i])*pow(b, mid-1, mod1)
        hash1 %= mod1

        hash2 -= ord(s[i-mid])
        hash2 *= pow(b, mod2-2, mod2)
        hash2 %= mod2
        hash2 += ord(s[i])*pow(b, mid-1, mod2)
        hash2 %= mod2
        if hash1 in t1 and hash2 in t2:
            ans = mid
            o = mid+1
            f = True
            break
        t1.add(hash1)
        t2.add(hash2)
    if not f: x = mid-1
print(ans)