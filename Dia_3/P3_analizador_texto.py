texto = str(input("Bienvenido/a, ingrese su texto para analizar: "))
letras = input("Ahora ingrese 3 letras para que busquemos.\nSepárelas con un espacio cada una: ")
#Veces que aparecen
texto = texto.lower()
letras = letras.lower()
lista_letras = letras.split()
cant_0= texto.count(lista_letras[0])
cant_1= texto.count(lista_letras[1])
cant_2= texto.count(lista_letras[2])
print(f"Hay {cant_0} caracteres {lista_letras[0]},{cant_1} caracteres {lista_letras[1]},\n{cant_2} caracteres {lista_letras[2]} en tu texto ")

#Cuenta palabras
lista_texto = texto.split()
cant_palabras = len(lista_texto)
print(f"Tu texto tiene {cant_palabras} palabras")

#Primera y ultima letra
print(f"La primera letra de tu texto es {texto[0]}.\nMientras que la última es {texto[-1]}")

#Mostrar texto invertido
lista_texto.reverse()
texto_revertido = " ".join(lista_texto)
print(f"Tu texto invertido tiene esta pinta:\n{texto_revertido}")

#Se encuentra la palabra python en el texto ?

resultado = "python" in texto
dic = {True:"Si se encuentra", False:"No se encuentra"}
print(f"La palabra 'Python' {dic[resultado]} en el texto")