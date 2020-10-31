#Video 37 - Archivos Externos
from io import open
#Abre archive
archivo=open("Archivos/archivo.txt","w")
frase="Hola mundo"
#Escribe archivo
archivo.write(frase)
#Cierra archivo
archivo.close()

#Lee archive
archivo_texto=open("Archivos/archivo.txt","r")
texto=archivo_texto.read()
archivo_texto.close()
print(texto)

#Ponerlo en lista
archivo_lista=open("Archivos/archivo.txt","r")
lineas_texto = archivo_lista.readlines()
archivo_lista.close()
print(lineas_texto)

#Agregar linea de texto
agregar_texto=open("Archivos/archivo.txt","a")
agregar_texto.write("\nSegunda Linea")
agregar_texto.close()

#Video 38 - Archivos Externos II
#Agregar linea de texto
texto=open("Archivos/archivo.txt","r")
print(texto.read())
#Desplaza puntero
texto.seek(5)
print(texto.read())

#Leer y escribir 
texto=open("Archivos/archivo.txt","r+")
texto.write("comiezo")
print(texto.read())

#Modificar lineas
archivo_texto=open("Archivos/archivo.txt","r+")
lista_texto=archivo_texto.readlines()
lista_texto[1]="Linea exterior \n ojojoj"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()
