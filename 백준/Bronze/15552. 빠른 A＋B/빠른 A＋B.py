import sys

input = sys.stdin.readline()

n = int(input)
nlist = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    nlist.append(a+b)

print(*nlist, sep="\n")