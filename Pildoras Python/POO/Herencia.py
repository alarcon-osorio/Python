#Video 29 - POO VI Herencia
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

class Moto(Vehiculos): #Video 29 Hreencia
    pass

miMoto = Moto("Honda", "CB190")
miMoto.estado()