# Listas por teclado
print('Listas por teclado')
lista = []
valor = int(input('Ingrese valores ' + '-0 para finalizar: '))
while valor != 0:
    lista.append(valor)
    valor = int(input('Ingrese valores ' + '-0 para finalizar: '))

#Imprimo los valores ingresados por teclado
print('Imprimo los valores ingresados por teclado ')
print(lista)
print('Imprimo el tamaño de la lista que ingrese: ' + str(len(lista)))


