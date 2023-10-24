lista = ['a','b','c']

for letra in lista:
    numero_letra =lista.index(letra) + 1
    print(f"Letra {numero_letra} es: {letra}")

lista_nom = ['pablo','laura','fede','luis','julia']

for nombre in lista_nom:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('Nombre que no comienza con l')

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)

palabra = 'python es genial'

for letra in palabra:
    print(letra)

for a,b in [[1,2],[4,6],[7,8]]:
    print(a)
    print(b)

dic = {'clave':'a','clave2':'b','clave3':'c'}
for item in dic.values():
    print(item)
for a,b in dic.items():
    print(a,b)

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for num in lista_numeros:
    if num % 2 == 0:
        suma_pares = suma_pares + num
    else:
        suma_impares = suma_impares + num