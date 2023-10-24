monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo mas dinero")

numero = 10

while numero > 0:
     print(numero)
     numero = numero - 1
else:
    print(numero)

numero1 = 50

while numero1 > 0:
    if numero1 % 5 == 0:
        print(numero1)
        numero1 -= 1
    else:
        numero1 -= 1
        continue

else:
    print(numero1)
nombre = input("Ingresa tu nombre: ")

for letra in nombre:
    if letra =='r':
        break
    print(letra)

for letra in nombre:
    if letra =='r':
        continue
    print(letra)

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for num in lista_numeros:
    if num <0:
        break
    else:
        print(num)