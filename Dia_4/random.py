from random import *

aleatorio =randint(1,50)
print(aleatorio)

aleatorio1 =round(uniform(1,50),1) #Decimal largo
print(aleatorio1)

aleatorio2 =random() #Entre 0 y 1 decimal
print(aleatorio2)

colores = ['verde','azul','rojo','purple']
aleatorio3 =choice(colores)
print(aleatorio3)

numeros = list(range(5,50,5)) #Mezcla aleatoria no se puede almacenar
shuffle(numeros)#...en una lista, cambia la lista. No strings
print(numeros)