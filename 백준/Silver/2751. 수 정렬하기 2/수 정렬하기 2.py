import sys
input = sys.stdin.readline

n = int(input())
nlist = []

for i in range(n):
    nlist.append(int(input()))

for i in sorted(nlist):
    print(i)