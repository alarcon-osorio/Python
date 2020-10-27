#Video 26 POO III -- Clase Coche
class Coche():
    #Video 27 - Declarando Constructor
    def __init__ (self): #Contructor de la clase
        #Propiedades
        self.largoChasis = 250
        self.anchoChasis = 120
        self.__ruedas = 4 #Video 27 -- self.__ encapsulo las variables
        self.enMarcha = False

    #Metodos - Comportamientos - los metodos pertenecesn a la clase, las funciones no 
    #Video 27 POO IV --- arrancamos, se borra codigo aterior
    def arrancar(self, arrancamos):
        self.enMarcha=arrancamos

        if self.enMarcha:
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un acho de ", self.anchoChasis)
        

miCoche=Coche() #Instanciamos la clase
print(miCoche.arrancar(True)) #Video 27
print(miCoche.estado())

#Video 27 POO IV -- Segunda instancia 
print("-------------Acontinuación Coche 2---------------")

miCoche2=Coche()#Video 27 -- Segunda instancia 
print(miCoche2.arrancar(False))
miCoche2.__ruedas = 2
print(miCoche2.estado())