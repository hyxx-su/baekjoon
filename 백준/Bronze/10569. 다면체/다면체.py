t = int(input())
tlist = []

for i in range(t):
    v, e = map(int, input().split())
    tlist.append(e-v+2)

print(*tlist, sep="\n")