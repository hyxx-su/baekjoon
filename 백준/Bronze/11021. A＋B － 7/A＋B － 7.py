n = int(input())
nlist = []

for i in range(n):
    a, b = map(int, input().split())
    nlist.append(a+b)

for i in range(1, n+1):
    print(f'Case #{i}: {nlist[i-1]}')