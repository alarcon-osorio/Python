#Funcion tipo f
for i in range(5,50,3): # empeiza en 5 termina en 49 y va de 3 en 3
    print(f"Valor de la variable {i}") # Concatena el tipo de la variable con el texto 

#Funcion len
nombre="Jeison"
for i in range(len(nombre)):
    print(f"Cantidad letras de mi nombre {i}")

valido = False
email = input("Introduce tu email: ")

for i in range(len(email)):
    if email[i] == "@":
        valido = True

if valido:
    print("Email Correcto")
else:
    print("Email incorrecto")