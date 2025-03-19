import sys, os, io

def main():
    mod = 10**9+7
    io.BufferedReader(io.FileIO(0), buffer_size=131072)
    def mat_mul_2(a, b):
        return [
            (a[0][0]*b[0] + a[0][1]*b[1]),
            (a[1][0]*b[0] + a[1][1]*b[1])
        ]
    def mat_mul(a, b):
        return [
            [(a[0][0]*b[0][0] + a[0][1]*b[1][0]), (a[0][0]*b[0][1] + a[0][1]*b[1][1])],
            [(a[1][0]*b[0][0] + a[1][1]*b[1][0]), (a[1][0]*b[0][1] + a[1][1]*b[1][1])]
        ]


    def mat_pow(a, n):
        result = [[1, 0], [0, 1]]
        while n:
            if n&1: result = mat_mul(result, a)
            a = mat_mul(a, a)
            n>>=1
        return result

    def c(n):
        if not n: return 1
        if n in cache:
            return cache[n]
        cache[n] = mat_mul_2(mat_pow(first, n-1), [-1,1])[1]
        return cache[n]


    ans = []
    cache = {}
    first = [[1,-1],[4,1]]
    it = map(int, os.read(0, os.fstat(0).st_size).split())
    n = next(it)
    #for i in it:
        #j, k = next(it), next(it)
        #pow5k = pow(5, k, mod)
        #ans.append(str(((((pow5k*((c(k*j)-c(k*(i-1))))%mod)%mod-c(k*(j+1))+c(k*i))%mod)*pow(pow5k+1-2*c(k), mod-2, mod))%mod))
    os.write(1, str(c(n)).encode())
    os._exit(0)

if __name__ == "__main__":
    main()