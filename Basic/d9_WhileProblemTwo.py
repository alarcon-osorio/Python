x = 0
suma = 0
while x < 5:
    valor = int(input("Ingrese valor " + str(x + 1) + ": "))
    suma = suma + valor
    x = x + 1
promedio = suma / 5
print("La suma de los valores es: " + str(suma))
print("El promedio de los valores es: " + str(promedio))
