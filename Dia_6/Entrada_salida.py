mi_archivo = open('Prueba.txt')
print(mi_archivo.read())
'''for l in mi_archivo:
    print("Aqui dice: " + l)

una_linea= mi_archivo.readline()
print(una_linea)
una_linea= mi_archivo.readline()
print(una_linea.rstrip())#quita el espacio entre lineas
una_linea= mi_archivo.readline()
print(una_linea)
mi_archivo.close()'''
'''todas = mi_archivo.readlines() #crea lista de lineas
todas = todas.pop()
print(todas)
'''
#Se pueden utilizar metodos de strings

#Elegir que linea imprimir al seleccionar lista
mi_archivo=open('texto.txt')
todas=mi_archivo.readlines()
print (todas[1])

