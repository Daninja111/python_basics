palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)
print(lista)

lista2 = [letra for letra in palabra]

print(lista2)

lista3 = [n for n in range(0,21,2)]
print(lista3)

lista4 = [n/2 for n in range(0,21,2)]
print(lista4)

lista5 = [n for n in range(0,21,2) if n*2 > 10]
print(lista5)

lista5 = [n if n*2 > 10 else 'no' for n in range(0,21,2) ]
print(lista5)
temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(gradosf - 32)*(5/9) for gradosf in temperatura_fahrenheit]