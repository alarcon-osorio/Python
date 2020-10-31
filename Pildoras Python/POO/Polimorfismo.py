#Video 32 POO IX - Polimorfismo
class Coche():
    def desplazamiento(self):
        print("Me desplazo usando 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo usando 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo usando 6 ruedas")

#Polimorfismo - sabe que metodo llama
def desplazamientoVehiculos(vehiculo):
    vehiculo.desplazamiento()

#Se instancia por medio del parametro
vehiculo=Camion()  # Se puede cambiar el objeto a Moto(), Coche()
desplazamientoVehiculos(vehiculo)
