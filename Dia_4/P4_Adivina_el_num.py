from random import *
aleatorio = randint(1,101)

nombre = input("¡Bienvenido/a! Ingresa tu nombre: ")

numero = int(input(f"Un gusto de tenerte aquí {nombre}.\n"
      f"Piensa un número del 1 al 100 y así lograr adivinar el número.\n"
      f"Ingresa aquí: "))
intentos = 8

while intentos > 0:
      if numero < 1 or numero > 100:
            print("El número ingresado es inválido.")
            numero = int(input("Intenta nuevamente: "))
            intentos-=1
      elif numero < aleatorio:
            print("El número ingresado es menor al número secreto.")
            numero = int(input("Intenta nuevamente: "))
            intentos -= 1
      elif numero > aleatorio:
            print("El número ingresado es mayor al número secreto.")
            numero = int(input("Intenta nuevamente: "))
            intentos -= 1
      else:
            print("¡Has ganado!")
            print(f"Lo lograste en {8-intentos} intentos")
            break
else:
      print("¡Has perdido! No te quedan más intentos")

#Como mejora del codigo el numero pedido puede ir dentro del while en general
#asi no preguntarlo en cada condicional al igual que el decremento.
