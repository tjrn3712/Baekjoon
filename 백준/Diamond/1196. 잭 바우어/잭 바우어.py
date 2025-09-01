import sys
from decimal import Decimal, getcontext
input = sys.stdin.readline
getcontext().prec = 200
g = Decimal("0.57721566490153286060651209008240243104215933593992")
def minput(): return map(int, input().split())


def H(x: int) -> Decimal:
    if x==0: return Decimal(0)
    if x < 100000:
        s = Decimal(0)
        for i in range(1, x+1):
            s += Decimal(1)/Decimal(i)
        return s
    return Decimal.ln(Decimal(x)) + g + (Decimal(1)/Decimal(2*x)) - (Decimal(1)/Decimal(12*x*x)) + (Decimal(1)/Decimal(120*x**4)) - (Decimal(1)/Decimal(252*x**6)) + (Decimal(1)/Decimal(240*x**8)) - (Decimal(1)/Decimal(132*x**10)) + (Decimal(691)/Decimal(32760*x**12))


n, k = minput()
print(Decimal(n)*(H(n)-H(n-k)))