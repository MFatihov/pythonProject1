def div(x):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

m = 0
for x in range(452022,500000):
    d = div(x)
    if len(d) > 0:
        m = d[0] + d[-1]
        if m >0:
            if m % 7 == 3:
                print(x,m)
