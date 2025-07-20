h, m = map(int, input().split())
a = int(input())
b = (m+a)//60
c = (m+a)%60

h+=b

if h<23:
    print(h, c)
else:
    h = h%24
    print(h, c)