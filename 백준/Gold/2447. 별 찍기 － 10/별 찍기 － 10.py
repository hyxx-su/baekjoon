def draw_stars(n):
    if n==1:
        return ["*"]
    
    stars = draw_stars(n//3)
    lists = []

    for i in stars:
        lists.append(i*3)
    for i in stars:
        lists.append(i+" "*(n//3)+i)
    for i in stars:
        lists.append(i*3)
    return lists

n = int(input())
print("\n".join(draw_stars(n)))