print("Programa de becas por Año 2020")
distancia_escuela=int(input("Introduce distancia: "))
print(distancia_escuela)

numero_hermanos=int(input("introduce Hermanos: "))
print(numero_hermanos)

salario_familiar=int(input("introduce Salario: "))
print(salario_familiar)

#AND, OR -- minusculas
if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
    print("Tienes derecho a beca")
else:
    print("Sin Derecho a Beca")

###################-----------------------------####################
#Funcion in -- Case sensitive 
#lower: minusculas
#upper: mayusculas
print("Asignatura por Año 2020")
opcion = input("Asignatura Escogida: ")
asignatura= opcion.lower()
if asignatura in ("informatica", "pruebas", "psabilidad"): #Todo lo pongo en minuscula
    print("Asignatura escogida " + asignatura)
else:
    print("No escogida")
