nlist = []

while True:
    try:
        n = float(input())
        if n > 0:
            nlist.append(f'Objects weighing {n:.2f} on Earth will weigh {n*0.167:.2f} on the moon.')
        else:
            break
    except:
        break

print(*nlist, sep="\n")