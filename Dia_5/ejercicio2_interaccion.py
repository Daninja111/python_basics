lista_numeros = [1, 2, 15, 7, 2, 8]


def reducir_lista(lista):
    print(lista)
    lista = list(set(lista)) #al ser set elimina dupli
    lista.sort() #ordena de menor a mayor
    lista.pop(-1) #elimina el ultimo
    return lista


def promedio(lista):
    valor_medio = sum(lista) / len(lista)
    return valor_medio

reducir_lista(lista_numeros)