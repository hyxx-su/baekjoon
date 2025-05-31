nlist = []
m = 10
cnt = 0

for i in range(10):
    n = int(input())
    n = n % 42
    if n in nlist:
        cnt += 1
    else:
        nlist.append(n)

print(m-cnt)