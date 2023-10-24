import os
from pathlib import Path
'''ruta = os.getcwd()
print(ruta)
ruta = os.chdir('C:\\Users\\mazzi\\Documents\\Python\\Dia_6\\Otra_ruta')
archivo = open('otro_archivo.txt','r')
print(archivo.read())
ruta = os.makedirs('C:\\Users\\mazzi\\Documents\\Python\\Dia_6\\Otra_ruta\\Otra')'''

ruta1 = 'C:\\Users\\mazzi\\Documents\\Python\\Dia_6\\Prueba.txt'
elemento = os.path.basename(ruta1)
elemento2 = os.path.dirname(ruta1)
elemento3 = os.path.split(ruta1)#Da los dos elementos en una tupla
print(elemento,elemento2)
'''os.rmdir('C:\\Users\\mazzi\\Documents\\Python\\Dia_6\\Otra_ruta\\Otra')'''
#rmdir elimina el directorio final
#Forma de abrir en cualquier sistema operativo

carpeta = Path('C:/Users/mazzi/Documents/Python/Dia_6/Otra_ruta')
archivo = carpeta / 'otro_archivo.txt' #Importar un archivo

mi_archivo=open(archivo)
print(mi_archivo.read())

