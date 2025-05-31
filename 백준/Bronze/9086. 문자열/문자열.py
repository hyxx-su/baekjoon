n = int(input())
mlist = []

for i in range(n):
    m = input()
    mlist.append(f'{m[0]}{m[-1]}')

print(*mlist, sep="\n")