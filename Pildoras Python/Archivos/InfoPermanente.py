#Video 41 - Guardado Permanente 
import pickle

class Persona():
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre: ", self.nombre)
    
    def __str__ (self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListarPersonas():
    personas=[]

    def __init__(self):
        listaDePersonas=open("Archivos/archivoExterno", "ab+")
        listaDePersonas.seek(0)

        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del archivo externo ".format(len(self.personas)))

        except:
            print("El fichero esta vacio")
        
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasArchivo()

    def mostrarPersona(self):
        for p in self.personas:
            print(p)

    def guardarPersonasArchivo(self):
        listaDePersonas=open("Archivos/ArchivoExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoArchivo(self):
        print("La informacion del archivo es la siguiente: ")
        for p in self.personas:
            print(p)


miLista=ListarPersonas()
persona=Persona("Antonio", "Masculino", "30")
miLista.agregarPersonas(persona)
miLista.mostrarInfoArchivo()