n = int(input())
nlist = []

for i in range(n):
    a, b, c = map(int, input().split())
    m = a * (c - 1) + b
    nlist.append(m)

print(*nlist, sep="\n")