

def chequear_3_cifras(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)

        else:
            pass
    return lista_3_cifras
resultado = chequear_3_cifras([574,45,999])
print(resultado)


lista_numeros = [5,-3,6,10]
def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n<0:
            return False
        else:
            pass
    return True

lista_numero2 = []
def suma_menores(lista_numeros2):
    suma = 0

    for n in lista_numeros2:
        if n in range(0, 1000):
            suma = suma + n

        else:
            pass
    return suma


lista_numeros1 = []

def cantidad_pares(lista_numeros1):
    cantidad = 0
    for n in lista_numeros1:
        if n % 2 == 0:
            cantidad += 1
        else:
            pass 
    return cantidad

