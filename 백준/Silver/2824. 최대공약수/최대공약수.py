import sys, math
input = sys.stdin.readline
sys.set_int_max_str_digits(100000)
def minput(): return map(int, input().split())

n = int(input())
a = [*minput()]
m = int(input())
b = [*minput()]

m1=m2=1
for i in range(n): m1*=a[i]
for i in range(m): m2*=b[i]
print(str(math.gcd(m1,m2))[-9:])