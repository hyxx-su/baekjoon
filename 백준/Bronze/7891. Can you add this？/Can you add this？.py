n = int(input())
nlist = []

for i in range(n):
    a, b = map(int, input().split())
    nlist.append(a+b)

print(*nlist, sep="\n")