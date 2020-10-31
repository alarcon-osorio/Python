#Video 39 - Serializacion 
import pickle

lista_nombres = ["Pedro", "Ana", "Maria", "Jeison"]
# wb binario
archivo_binario=open("Archivos/archivo_binario.txt", "wb")
#pone info
pickle.dump(lista_nombres, archivo_binario)
archivo_binario.close()
del(archivo_binario)

archivo=open("Archivos/archivo_binario.txt", "rb")
#carga info
lista=pickle.load(archivo)
print(lista)