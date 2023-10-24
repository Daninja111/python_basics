lista = ['a','b','c']
indice = 0

for item in lista:
    print(indice, item)
    indice += 1

for indice,item in enumerate(lista):
    print(indice, item)
for item in enumerate(lista):
    print(item)

for item in enumerate(range(50,55)):
    print(item)

mis_tuples = list(enumerate(lista))
print(mis_tuples)

palabra = list(enumerate('Python'))
print(palabra)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(indice)
    else:
        continue