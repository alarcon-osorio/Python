########
#i=1
#while i <= 10:
#    print("Ejecucion" + str(i)) #Bucle infitinito 

#print("Termino la ejecucion")
#########

## Ejemplo 1
i=1
while i <= 10:
    print("Ejecucion" + str(i)) 
    i=i+1 #Contador para que la tome False y salga del infinito

print("Termino la ejecucion")

## Infinito para edad correcta
edad = int(input("Introduce Edad por favor: "))
while edad < 0 or edad > 100:
    print("Error de edad")
    edad = int(input("Introduce Edad por favor: "))

print("Termino la ejecucion, la edad de la persona es: " + str(edad))

## Ejemplo 2 --- importar Clase 
import math
numero = int(input("Introduce un numero por favor: "))
intentos = 0

while numero < 0:
    print("No se puede hallar la raiz de un numero negativo")

    if intentos == 2:
        print("has consumido demasiados intento")
        break

    numero = int(input("Introduce un numero por favor: "))
    if intentos < 0:
        intento = intento +1 

if intentos < 2:
    solucion = math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))