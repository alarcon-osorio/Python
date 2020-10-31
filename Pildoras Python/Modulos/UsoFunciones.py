#Video 34
#Import tradicional 
import FuncionesMatematicas as funciones

funciones.sumar(7,5)
funciones.restar(7,5)
funciones.multiplicar(7,5)

##Importar solo una 
from FuncionesMatematicas import sumar 

sumar(7,5)

###Utilizar todo - Importar todo
from FuncionesMatematicas import * 
sumar(7,5)
restar(7,5)
multiplicar(7,5)

