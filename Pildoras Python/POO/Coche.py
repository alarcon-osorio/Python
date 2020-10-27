class Coche():
    #Propiedades
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False

    #Metodos - Comportamientos - los metodos pertenecesn a la clase, las funciones no 
    def arrancar(self):
        self.enMarcha = True

    def estado(self):
        if self.enMarcha:
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
        

miCoche=Coche() #Instanciamos la clase
print("El largo del coche es: ", miCoche.largoChasis)
print("El coche tiene: ", miCoche.ruedas, " ruedas" )
miCoche.arrancar()
print(miCoche.estado())