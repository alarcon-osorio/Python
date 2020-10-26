#Imprime las letras de un escrito
for letra in "Python":
    print("Letras de Python = " + letra)

#Continue - sin h
print("Python sin h")
for letra in "Python":
    if letra == "h":
        continue
    print("Letras de Python = " + letra)

#Cantidad de caracteres 
mensaje="hola mundo"
print(len(mensaje))

#Cantidad de caracteres -- continue a pesa rde espacios en blanco
mensaje="hola mundo"
contador = 0
for i in mensaje:

    if i == " ":
        continue
    contador+=1

print(contador)

#pass
#while True:
#    pass

#class MiClase:
#    pass #Para implemetar mas tarde 

## Ejemplo 3
email = input("Introduce tu email: ")
for i in email:
    if i == "@":
        arroba = True
        break

else: #No forma parte del if si no del for
    arroba = False

print(arroba)