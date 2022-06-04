lista = []
lista_1 = []
lista_2 = []
lista_3 = []
i = 0

n = int(input('').strip())
while i < n:
    lista.append(0)
    i+=1
    lista_1.append(i)
    n1 = int(input('').strip())
    lista_2.append(n1)
x = 0
while x < n:
    n2 = int(input('').strip())
    x+=1
    lista_3.append(n2)
print(lista)
print(lista_1)
print(lista_2)
lista_3.reverse()
print(lista_3)
