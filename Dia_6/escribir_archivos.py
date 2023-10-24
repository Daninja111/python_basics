'''mi_texto=open('Prueba.txt', 'w')
mi_texto.write('soy el nuevo texto') #sobreescribe sin dejar lo anterior
mi_texto.writelines(['hola','mundo','aqui','estoy']) #escribe todo junto
mi_texto.close()'''

archivo = open("mi_archivo.txt","a")
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open("mi_archivo.txt","r")
print(archivo.read())

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
registro = "\t".join(registro_ultima_sesion)
archivo = open('registro.txt', 'a')
archivo.write(registro)
archivo.close()
archivo = open('registro.txt', 'r')
print(archivo.read())