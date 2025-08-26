import sys, math
from decimal import Decimal, getcontext
input = sys.stdin.readline
getcontext().prec = 100
lnpi = (Decimal(2).ln()+Decimal('3.14159265358979323846264338327950288419716939937510').ln())
def minput(): return map(int, input().split())


def lnfact(n: int)->Decimal:
    if n<9999: return Decimal(math.factorial(n)).ln()
    nDec = Decimal(n)
    return (Decimal('0.5')*(lnpi+nDec.ln()))+nDec*(nDec.ln()-1)+(Decimal(1)/(12*nDec))-(Decimal(1)/(360*nDec**3))+(Decimal(1)/(1260*nDec**5))-(Decimal(1)/(1680*nDec**7))+(Decimal(1)/(1188*nDec**9))-(Decimal(691)/(360360*nDec**11))+(Decimal(1)/(156*nDec**13))


r, b = minput()
log = (Decimal(r)+Decimal(b))*Decimal(2).ln()-lnfact(r+b)+lnfact(r)+lnfact(b)
if log > Decimal(0.99e9).ln(): exit(print("Extreme Wealth"))
ans = log.exp()
print(ans)