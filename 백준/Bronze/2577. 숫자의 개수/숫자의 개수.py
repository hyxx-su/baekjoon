a = int(input())
b = int(input())
c = int(input())

n = a*b*c

m = list(str(n))
cnt = 0

for i in range(10):
    cnt = 0
    for ii in m:
        if i == int(ii):
            cnt += 1
    print(cnt)