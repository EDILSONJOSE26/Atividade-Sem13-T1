lista = []
l_par = []
l_impar = []
for i in range(20):
    n = int(input('').strip())
    lista.append(n)
    if n % 2 == 0:
        l_par.append(n)
    else:
        l_impar.append(n)
print(lista)
print(l_par)
print(l_impar)
