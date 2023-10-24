#Definir funciones con argumentos variables en num
def suma(*args): #args puede tener otro nombre
    total = 0

    for arg in args:
        total += arg    #lineas 5 a 7 pueden ser reemplazadas por
    return total        #return sum(args)

print(suma(5,6,7,8))



