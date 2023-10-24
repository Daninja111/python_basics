def mi_generador():
    num = 0
    while True:
        yield num
        num += 1


generador = mi_generador()
next(generador)