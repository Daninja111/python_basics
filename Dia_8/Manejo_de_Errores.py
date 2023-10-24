'''def suma():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print(n1+n2)
    print("Gracias por sumar")
try:
    # Codigo que queremos probar
    suma()
except:
    print("Algo no funcinó")
    # Codigo a ejecutar si hay error
else:
    # Codigo a ejecutar
    print("Hiciste todo bien")
finally:
    #Codigo que se va a ejecutar
    print("Eso fue todo")'''

def pedir_numero():

    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un número")
        else:
            print(f"Ingresaste el número {numero}")
            break
    print("Gracias")

pedir_numero()