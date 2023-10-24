import os
from pathlib import Path
from os import system
mi_ruta = Path(Path.home(), "Recetas")

def contar_recetas(ruta):
    contador=0
    for txt in Path(ruta).glob("**/*.txt"):
        contador+=1
    return contador
def inicio():



def bienvenida():
    nombre = input(f"Ingresa tu nombre: ")
    print(f"Bienvenido/a {nombre} al Recetario")
    #Dar ruta de acceso
    #Dar numero de recetas

def opciones():
    opcion_elegida=''
    es_valida=False
    num_opciones='123456'

    while not es_valida:
        print(f"¿Que quieres hacer?\n1) Leer Receta\n2) Crear Receta\n3) Crear Categoría\n4) Eliminar Receta\n5) Eliminar Categoría\n6) Finalizar programa")
        opcion_elegida = input("Ingresa el número de tu opción: ")
        if opcion_elegida in num_opciones and len(opcion_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una opción válida")
    return opcion_elegida

#opcion 1 LEER RECETA
'''def leer_receta():


#opcion 2 CREAR RECETA
def crear_receta():

#opcion 3 CREAR CATEGORIA
def crear_categoria():

#opcion 4 ELIMINAR RECETA
def eliminar_receta():

#opcion 5 ELIMINAR CATEGORIA
def eliminar_categoria():

#opcion 6 FINALIZAR PROGRAMA
def finalizar_prog():'''



#Ejecucion del programa
'''bienvenida()
opciones()'''
ruta = os.getcwd()
print(ruta)
