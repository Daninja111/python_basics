def mi_generador():
    num = 3
    while True:
        if num == 3:
            yield "Te quedan 3 vidas"
        elif num == 2:
            yield "Te quedan 2 vidas"
        elif num == 1:
            yield "Te queda 1 vida"
        elif num == 0:
            yield "Game Over"
        num -= 1


perder_vida = mi_generador()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))


'''def mensaje():
    x = "Te quedan 3 vidas"
    yield x

    x = "Te quedan 2 vidas"
    yield x

    x = "Te queda 1 vida"
    yield x

    x = "Game Over"
    yield x


perder_vida = mensaje()'''