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

#Video 30  POO VII Herencia II
class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargar=cargar
        if cargar:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class Moto(Vehiculos): #Video 29 Hreencia
    #Video 30  POO VII Herencia II - Sobrescritura de metodos
    hstunt=""
    def stunt(self):
        self.hstunt="Hago Stunt con mi moto"

    #Video 30  POO VII Herencia II - Se sobre escribe le metodo de la clase padre 
    def estado(self):
        print("Marca:", self.marca, "\nModelo:",self.modelo ,"\nEn Marcha", self.enMarcha,
        "\nAcelerando",self.acelera,"\nFranando",self.frena, "\n",self.hstunt)

class Electricos():
    def __init__(self):
        self.autonomia=100
        
    def cargarEnergia(self):
        self.cargando = True

miMoto = Moto("Honda", "CB190")
miMoto.stunt()
miMoto.estado()
print("----Furgoneta-----")
miFurgoneta=Furgoneta("Mazda", "Hargi")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))
print("----Electricos-----")

class BicicletaElecrtica(Electricos, Vehiculos): #Herencia multiple
    pass
print("----Bicicleta Elecrtica-----")
miBici = BicicletaElecrtica() #Hereda siempre el primer constructor por preferencia indicado en la clase de la herencia multiple

