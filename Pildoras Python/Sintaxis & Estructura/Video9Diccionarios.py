miDiccionario={"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "Colombia":"Bogota"}
#Clave especifica
print(miDiccionario["Colombia"])
#Todo el diccionario
print(miDiccionario)
#Agregar nuevo elemento
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)
#Corregir valor - Se sobreescribe
miDiccionario["Italia"]="Roma"
print(miDiccionario)
#Eliminar Clave - Valor
del miDiccionario["Italia"]
print(miDiccionario)
#Varios tipos de datos y con tupla
miTupla=["Alemania","Francia", "Reino Unido", "Colombia"]
miDiccionario={miTupla[0]:"Berlin", miTupla[1]:"Paris", miTupla[2]:"Londres", miTupla[3]:"Bogota"}
print(miDiccionario)
#Poner tuplas en Claves
miDiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":[1991,1992,1993,1994,1995]}
print(miDiccionario["Anillos"])
#Diccionario en otro Diccionario
miDiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"Temporadas":[1991,1992,1993,1994,1995]}}
print(miDiccionario["Anillos"])
#Metodos keys, values, len
print(miDiccionario.keys())
print(miDiccionario.values())
print(len(miDiccionario))