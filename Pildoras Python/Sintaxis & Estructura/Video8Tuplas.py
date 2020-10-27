miTupla=("JEISON",8,7,1990)
print(miTupla)
#Convertir tupla en lista lis
miLista=list(miTupla)
print(miLista)
#convertir rapidamente lista en tupla tuple
miLista=["JEISON",8,7,1990]
miTupla=tuple(miLista)
print(miTupla)
#Encontrar caracter en tupla in
miLista=["JEISON",8,7,1990]
miTupla=tuple(miLista)
print("JEISON" in miTupla)
#Encontratr cantidad de verces elemento count
miLista=["JEISON",8,7,1990,7]
miTupla=tuple(miLista)
print(miTupla.count(7))
#Averiguar longitud de tupla len
miLista=["JEISON",8,7,1990,7]
miTupla=tuple(miLista)
print(len(miTupla))
#Tuplas unitarias 
miLista=["JEISON"]
miTupla=tuple(miLista)
print(len(miTupla))
#Otras formas de tupla -  sin parentesis (Empaquetado de tupla)
miTupla="JEISON",8,7,1990,7
print(miTupla)
#Otras formas de tupla -  (Desesmpaquetado de tuplas)
miTupla=("JEISON",8,7,1990,7)
nombre, dia, mes, anio, number = miTupla # asigna los valores a las variables declaradas 
print(nombre)
print(dia)
print(mes)
print(anio)
print(number)