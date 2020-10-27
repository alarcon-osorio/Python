#Video 26 POO III -- Clase Coche
class Coche():
    #Video 27 - Declarando Constructor
    def __init__ (self): #Contructor de la clase
        #Propiedades
        self.largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 #Video 27 -- self.__ encapsulo las variables, accesible desde la propia clase
        self.enMarcha = False

    #Metodos - Comportamientos - los metodos pertenecesn a la clase, las funciones no 
    #Video 27 POO IV --- arrancamos, se borra codigo aterior
    def arrancar(self, arrancamos):
        self.__enMarcha=arrancamos #Video 28 

        #Video 28 
        if self.__enMarcha:
            chequeo = self.__checkInterno()

        if self.__enMarcha and chequeo: #Video 28 -- and chequeo y elif
            return "El coche esta en marcha"
        elif self.__enMarcha and chequeo == False:
            print("Algo esta mal en el chequeo, no podemos arrancar")
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un acho de ", self.__anchoChasis)

    #Video 28 POO V -- Encapsulacion de metodos
    def __checkInterno(self):
        print("Realizando Check Interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False
        
print("-------------Acontinuación Coche 1---------------")
miCoche=Coche() #Instanciamos la clase
print(miCoche.arrancar(True)) #Video 27
print(miCoche.estado())

#Video 27 POO IV -- Segunda instancia 
print("-------------Acontinuación Coche 2---------------")
miCoche2=Coche()#Video 27 -- Segunda instancia 
print(miCoche2.arrancar(False))
# miCoche2.__ruedas = 2 #Video 27 solo se puede acceder a este valor desde la clase //Video 28 -- se comenta miCoche2.__ruedas = 2
print(miCoche2.estado())