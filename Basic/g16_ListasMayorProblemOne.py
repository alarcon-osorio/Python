# Listas por teclado
lista = []
for x in range(5):
    mayor = int(input('Ingrese valor: '))
    lista.append(mayor)

mayor = lista[0]
for x in range (1,5):
    if lista[x] > mayor:
        mayor = lista[x]

print('Lista completa: ' + str(lista))
print('Mayor a esa lista: ' + str(mayor))

