#Declaracion de la lista
miLista=["Maria","Jesus","Pablo","Pedro"]
#Lista completa
print(miLista[:])
#Elemnto especifico
print(miLista[2])
#Si no Existe - Exception
# print(miLista[7])
print(miLista[-2]) #No da error al ser negativo le da la vuelta

#Listas muy largas - Porcion de listas
print(miLista[0:3]) #Los tres primeros indices deja excluido el 3
print(miLista[:3]) #Los tres primeros indices, se puede omitir el 0
print(miLista[2:]) #Los dos ultimos indices, hasta el final

#Agregar elementos append()
miLista.append("Miguel")
print(miLista[:])
#Agregar en punto intermedo insert()
miLista.insert(2,"Miguel")
print(miLista[:])
#Agregar mas lista sumada extend([])
miLista.extend(["Juan","Jose", "Camilo"])
print(miLista[:])
#Saber en que pocision esta un elemento index 
print(miLista.index("Juan"))
#Se encuentra o no en la lista in
print("Jeison" in miLista)
#Se almacenal varios tipos de datos 
miLista=[1,2,"Pablo","Pedro",2.2]
print(miLista[:])
#Eliminar elementos especificos remove 
miLista.remove(1)
print(miLista[:])
#Eliminar ultimo elemento pop 
miLista.pop()
print(miLista[:])
#Operador + para concatenar listas
miLista2 = ["Juan","Jose", "Camilo"]
miLista3 = miLista + miLista2 # concatenar lista 
print(miLista3)
#Operador * Repetir listas
miLista2 = ["Juan","Jose", "Camilo"] * 3
print(miLista[:])