def getCiudades(*ciudades): # * indica que recibira un numero indeterminado de elementos en forma de Tupla
    for elemento in ciudades:
        yield from elemento 
        #for subElemento in elemento:  # for anidado
        yield from elemento # for anidado con sintaxis yield from

ciudadesDevueltas = getCiudades("Bogota","Medellin","Cali","Pereira")
#Elemento 1
print(next(ciudadesDevueltas))
#Elemento 2
print(next(ciudadesDevueltas))