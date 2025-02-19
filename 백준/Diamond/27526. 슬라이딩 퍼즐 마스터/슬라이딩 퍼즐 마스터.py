import sys
input = sys.stdin.readline
def minput(): return map(int, input().split())


n, m = minput()
g = []
for i in range(n):
    g.append([str(j) if j!=n*m else '#' for j in range(m*i+1, m*i+m+1)])

arr = []
for i in range(n):
    arr += g[i] if ~i&1 else g[i][::-1]

perm = [[arr[0]]]
for i in range(1, n*m):
    new_perm = []
    for idx, p in enumerate(perm):
        L = len(p)
        if ~idx&1:
            for pos in range(L,-1,-1):
                new_perm.append(p[:pos]+[arr[i]]+p[pos:])
        else:
            for pos in range(L+1):
                new_perm.append(p[:pos] + [arr[i]]+p[pos:])
    perm = new_perm

out_lines = []
for p in perm:
    for j in range(n):
        temp = p[j*m:(j+1)*m] if ~j&1 else p[j*m:(j+1)*m][::-1]
        out_lines.append("".join(temp))
sys.stdout.write("\n".join(out_lines))
