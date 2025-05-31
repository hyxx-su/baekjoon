a, b, c = map(int, input().split())

n = 0

if a == b and a == c:
    n = 10000+a*1000
elif a == b or c == a:
    n = 1000+a*100
elif b == c:
    n = 1000+b*100
else:
    if a > b:
        if a > c:
            n = a*100
        else:
            n = c*100
    elif b > c:
        n = b*100
    else:
        n = c*100

print(n)