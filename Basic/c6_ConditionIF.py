# Condicionales Simples y compuestas
salario = int(input("Ingrese su salario: "))
if salario > 3000:
    print("Salario alto: " + str(salario))
    salario = int(input("Ingrese  salario: "))
else:
    print("Salario bajo: " + str(salario))

