n = input()
lol = 0
o = 0
u = 0
lista = []

first = False

for i in range(len(n)):
    if lol == 0:
        if n[i] == "-":
            u += 1
            o = int(n[:i])
            lista.append(o)
            lol = i + 1
            first = True
        elif n[i] == "+":
            o = int(n[:i])
            lista.append(o)
            lol = i + 1
    else:
        if n[i] == "-":
            o = int(n[lol:i])
            if first:
                lista.append(-o)
            else:
                lista.append(o)
            lol = i + 1
            u += 1
            first = True
        elif n[i] == "+":
            o = int(n[lol:i])
            if first:
                lista.append(-o)
            else:
                lista.append(o)
            lol = i + 1

o = int(n[lol:i+1])

if first:
    lista.append(-o)
else:
    lista.append(o)

a = sum(lista)
print(a)