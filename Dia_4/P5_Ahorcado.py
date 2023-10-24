from random import *
#Programa elige palabra entre una lista al azar
def palabra_secreta():
    lista_secreta = ['canario','mesa','avestruz','ventanal','lapicera','mate']

    return choice(lista_secreta)
seleccion=palabra_secreta()

#mostrar visualmente

def visual(seleccion):
    palabra_sep=list(seleccion)
    palitos=[]
    cant_letras=0
    for n in palabra_sep:
        palitos.append('_')
        visual = " ".join(palitos)
        cant_letras+=1
    print(visual)
    return cant_letras

cantidad_letras=visual(seleccion)
#pedir al usuario letra
def peticion_usuario():
    letra='x'
    while letra not in seleccion:
        letra = input("Ingrese una letra: ")
        letra.lower()
    return letra

letra_obtenida=peticion_usuario()

#validar letra

#chequear letra
'''def chequear_letra(seleccion,letra_obtenida):
    palabra_sep=list(seleccion)
    posicion=[]
    for letra in palabra_sep:
        if palabra_sep[indice]==letra_obtenida:
            posicion.append(palabra_sep.index(letra_obtenida))
            print("Si hay")
        else:
            pass
    print(posicion)
chequear_letra(seleccion,letra_obtenida)'''

#vidas y si gano
