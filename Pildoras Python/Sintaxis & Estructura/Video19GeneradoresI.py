def generaPares(limite):
    num = 1
    miLista = []
    while num<limite:
        miLista.append(num*2)
        num=num+1    
    return miLista

print(generaPares(10))

## Ejemplo 2 -yield
print("Ejemplo 2 -yield")
def generaPares2(limite):
    num = 1
    while num<limite:
        yield num*2 #Objeto iterable 
        num=num+1 

devuelvePares = generaPares2(10)
for i in devuelvePares:
    print(i)

## Ejemplo 3 -next
print("Ejemplo 3 -next")
def generaPares3(limite):
    num = 1
    while num<limite:
        yield num*2 #Objeto iterable 
        num=num+1 

devuelvePares = generaPares3(10) #Estado de suspension 
print(next(devuelvePares)) #Devuelve primer valor almacenado

print("Primer Linea de Codigo") 

print(next(devuelvePares)) #Devuelve primer valor almacenado