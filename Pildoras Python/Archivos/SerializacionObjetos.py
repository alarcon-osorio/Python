#Video 40 - Serializacion II
import pickle

class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False
    
    #comportamiento
    def arrancar(self):
        self.enMarcha = True
    
    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:",self.modelo ,"\nEn Marcha", self.enMarcha,
        "\nAcelerando",self.acelera,"\nFranando",self.frena)

coche1=Vehiculos("Mazda", "MX5")
coche2=Vehiculos("SEAT", "Optra")
coche3=Vehiculos("Renault", "Megane")

coches=[coche1,coche2,coche3]

archivo=open("Archivos/coches", "wb")
pickle.dump(coches, archivo)
archivo.close()
del(archivo)

archivoAbre=open("Archivos/coches", "rb")
misCoches=pickle.load(archivoAbre)
archivoAbre.close()
for c in misCoches: 
    print(c.estado())