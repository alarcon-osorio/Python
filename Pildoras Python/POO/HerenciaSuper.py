#Video31 - POO VIII Herencia III 
class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia
    
    def descripcion(self):
        print("Nombre: ", self.nombre, " Edad: ", self.edad, " Resisdencia: ", self.lugar_residencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado) #Metodo super para llamar a la clase constructora padre padre
        self.salario=salario
        self.antiguedad=antiguedad
    
    def descripcion(self):
        super().descripcion()
        print(" Salario: ", self.salario, " Antiguedad: ", self.antiguedad)

Antonio=Empleado(1500, 15, "Jeison", 30, "Colombia")
Antonio.descripcion()
print(isinstance(Antonio, Persona))