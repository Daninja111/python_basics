from random import randint

def lanzar_moneda():
    moneda=randint(0,1)
    if moneda == 0:
        return 'Cara'
    else:
        return 'Cruz'

lista_numeros = [1,5,7,3]

def probar_suerte(res,lista):
    if res=='Cara':
        lista.clear()
        print("La lista se autodestruirá")
        return lista
    else:
        print("La lista fue salvada")
        return lista
