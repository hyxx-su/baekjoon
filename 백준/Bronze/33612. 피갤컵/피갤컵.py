n = int(input())
y = 2024
m = 1

for i in range(n):
    m += 7

v = m // 13

if v:
    m -= v * 12
    y += v

print(y, m)