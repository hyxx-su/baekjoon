h, m = map(int, input().split())

if m>=45:
    m-=45
    print(h, m)
else:
    if h!=0:
        h-=1
        m+=15
        print(h, m)
    elif h==0:
        h=23
        m+=15
        print(h, m)