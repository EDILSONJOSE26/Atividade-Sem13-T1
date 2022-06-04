l_2 = []
l_3 = []
l_4 = []
i = 0
n = int(input('').strip())
while i < n:
    i += 1
    n1 = float(input('').strip())
    l_2.append(n1)

x = 0
while x < n:
    x += 1
    n2 = float(input('').strip())
    l_3.append(n2)
a = 0
vogais = 0
while a < n:
    a += 1
    n3 = str(input('').strip())
    if n3 in"AEIOUaeiou":
        vogais += 1
    else:
        l_4.append(n3)
l_2.reverse()
print(l_2)
print(l_3)
if n == 0:
    print('SEM NOTAS')
else:
    mean = sum(l_3)/len(l_3)
    print(f'{mean:.1f}')
print(vogais)
print(l_4)
    
