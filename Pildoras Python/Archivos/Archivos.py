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


