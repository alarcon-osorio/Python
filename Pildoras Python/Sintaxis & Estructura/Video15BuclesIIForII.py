# end "" Finaliza con espacio inexistente -- end " " finaliza con espacio existente
for i in ["Hola", "mundo", 3]:
    print("hola", end="") 
    print("hola", end=" ") 

#Recorrer tantas veces como caracteres existen
for i in "alarcon_osorio@hotmail.com":
    print("hola")

#Saber si es correcto email # Los booleanos son el mayus la inicial
email = False
miEmail = input("Introduce email: ")
for i in miEmail:
    if i == "@" and i == ".":
        email = True

if email == True:
    print("Email correcto")
else:
   print("Email incorrecto") 
   print(miEmail)

#range 
for i in range(5):
    print("Hola")
