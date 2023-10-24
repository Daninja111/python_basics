from random import *


def lanzar_dados():
    return randint(1, 6), randint(1, 6)


def evaluar_jugada(dado_1, dado_2):
    suma = dado_1 + dado_2

    if suma <= 6:
        return print(f"La suma de tus dados es {suma}. Lamentable")
    elif suma > 6 and suma < 10:
        return print(f"La suma de tus dados es {suma}. Tienes buenas chances")
    else:
        return print(f"La suma de tus dados es {suma}. Parece una jugada ganadora")
#invocacion
dado_1,dado_2=lanzar_dados()
evaluar_jugada(dado_1,dado_2)