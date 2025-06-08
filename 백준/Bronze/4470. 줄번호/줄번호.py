n = int(input())
nlist = []

for i in range(1, n+1):
    m = input()
    nlist.append(f'{i}. {m}')

print(*nlist, sep="\n")