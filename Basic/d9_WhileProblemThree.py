cantidad = 0
x = 0
n = int(input("Ingrese la cantidad: "))
while x < n:
    largo=float(input("Ingrese la medida de la pieza " + str(x + 1) + ": "))
    if largo>=1.2 and largo<=1.3:
        cantidad=cantidad+1
    x=x+1
print("La cantidad de piezas aptas son: " + str(cantidad))
