a = []
b = []
cont = 0
z = zip(a, b)

for c in range(1, 51):
    ele = int(input().strip())
    cont+=1
    if cont <= 25:
        a.append(ele)
    else:
        b.append(ele)


c = []
for i in range(25):
    c.append(a[i])
    c.append(b[i])
    
print(f'{a[:]}')
print(f'{b[:]}')
print(c)
