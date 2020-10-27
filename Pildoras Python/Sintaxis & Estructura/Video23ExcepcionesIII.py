def evaluaEdad(edad):
    if edad < 0:
        raise TypeError("No se permiten edades negativas")
    if edad < 20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres Maduro"
    elif edad<100:
        return "Cuidate..."

print(evaluaEdad(15)) # Si se pone numero negativo lanza la excepcion

###Ejemplo 2 ---

import math
def calculaRaiz(num1):
    if num1<0:
        raise ValueError("El numero no puede ser negatvo")
    else:
        return math.sqrt(num1)

op1=(int(input("Introduce numero: ")))
try:
    print(calculaRaiz(op1))
except ValueError as ErrorNumeroNegativo:
    print(ErrorNumeroNegativo)
print("Programa Termnado")
