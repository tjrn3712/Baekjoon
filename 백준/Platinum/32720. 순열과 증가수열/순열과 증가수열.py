import sys
input = sys.stdin.readline
mod = 10**9+7
def minput(): return map(int, input().split())


n, k = minput()
det = 1
fact = [1]
for i in range(1, n+1):
    fact.append(fact[i-1]*i%mod)

for i in range(1, k+1):
    det *= fact[(n-i)//k+1]
    det %= mod

print(fact[n]*pow(det, mod-2, mod)%mod)