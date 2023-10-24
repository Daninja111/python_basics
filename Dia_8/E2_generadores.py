'''Crea un generador (almacenado en la variable generador) que sea capaz
de devolver de manera indefinida múltiplos de 7, iniciando desde el mismo 7,
y que cada vez que sea llamado devuelva el siguiente múltiplo.'''

def mi_generador():
    num = 0
    while True:
        yield num * 7
        num += 1


generador = mi_generador()
next(generador)