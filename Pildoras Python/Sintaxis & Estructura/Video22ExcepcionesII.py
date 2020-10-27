def divide():
    try:

        op1=(float(input("Introduce el primer numero: ")))
        op2=(float(input("Introduce el primer numero: ")))
        
        print("La divide es: " + str(op1/op2))
        print("Calculo finalizado")
    
    #except: Forma general
    except ValueError:
        print("El valor introducido es erroneo")
    
    except ZeroDivisionError:
        print("No se puede dividir entre 0 ")

    finally:  #Es necesario y se ejecutara siempre        
        print("Calculo finalizado")

     


divide()