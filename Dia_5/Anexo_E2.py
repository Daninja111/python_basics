'''Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d','e','i','n','o','r','t']'''
def orden_alfa(palabra):
    lista_orden=[]
    lista_orden=list(palabra)
    pasa_a_set=set(lista_orden)
    lista_orden1=sorted(pasa_a_set)
    print(lista_orden1)
    return lista_orden1

orden_alfa('entretenido')