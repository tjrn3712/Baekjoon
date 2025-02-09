import sys
input = sys.stdin.readline
def minput(): return map(int,input())


mod1,mod2=10**9+7,998244353
b=257

t = list(input().rstrip())
p = list(input().rstrip())

if len(p) > len(t):
    exit(print(0))
p_hash1 = 0
p_hash2 = 0
tmp1 = 1
tmp2 = 1
for i in range(len(p)):
    p_hash1 += ord(p[i])*tmp1
    p_hash2 += ord(p[i])*tmp2
    p_hash1 %= mod1
    p_hash2 %= mod2
    tmp1 *= b
    tmp2 *= b
    tmp1 %= mod1
    tmp2 %= mod2


t_hash1 = 0
t_hash2 = 0
tmp1,tmp2=1,1
for i in range(len(p)):
    t_hash1 += ord(t[-len(p)+i])*tmp1
    t_hash2 += ord(t[-len(p)+i])*tmp2
    t_hash1 %= mod1
    t_hash2 %= mod2
    tmp1 *= b
    tmp2 *= b
    tmp1 %= mod1
    tmp2 %= mod2

ans = []
cnt = 0
if p_hash1 == t_hash1 and p_hash2 == t_hash2:
    ans.append(len(t)-len(p)+1)
    cnt += 1
for i in range(len(t)-len(p)):
    t_hash1 -= ord(t[-1-i]) * pow(b, len(p)-1, mod1)
    t_hash2 -= ord(t[-1-i]) * pow(b, len(p)-1, mod2)
    t_hash1 *= b
    t_hash2 *= b
    t_hash1 += ord(t[-1-len(p)-i])
    t_hash2 += ord(t[-1-len(p)-i])
    t_hash1 %= mod1
    t_hash2 %= mod2
    if p_hash1 == t_hash1 and p_hash2 == t_hash2:
        ans.append(len(t)-len(p)-i)
        cnt += 1
print(cnt)
print(*ans[::-1])