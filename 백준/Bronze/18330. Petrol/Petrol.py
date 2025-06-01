n = int(input())
m = int(input())

if n <= m+60:
    print(n*1500)
else:
    print((60+m)*1500+(n-m-60)*3000)