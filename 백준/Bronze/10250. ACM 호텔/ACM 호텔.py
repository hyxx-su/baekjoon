m = int(input())
nlist = []

for i in range(m):
    h, w, n = map(int, input().split())
    for ii in range(1, w+1):
        for iii in range(1, h+1):
            n -= 1
            if n == 0:
                if ii < 10:
                    nlist.append(f'{iii}0{ii}')
                else:
                    nlist.append(f'{iii}{ii}')
                    
print(*nlist, sep="\n")