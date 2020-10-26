#Valor por teclado
print("Programa NOTAS")
#Se debe castear un input si lo queremos numerico
nota_alumno=input("Introduce la nota: ")

#Condicional IF
def evaluacion(nota):
    valoracion="Aprobado"
    if nota<5:
        valoracion = "Reprobado"
        #calificacion = 7 #Solo accesible desde el IF - Aclaración
    return valoracion

print(evaluacion(int(nota_alumno)))