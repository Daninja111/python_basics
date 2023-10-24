texto = "Este es el texto de Dani"

resultado = texto.upper()
resultado2 = texto[2].upper()
resultado3 = texto.lower()
resultado4 = texto.split()
resultado5 = texto.split("t")
print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)

resultado6 = texto.find("x")
print(resultado6)

resultado7 = texto.replace("Dani", "Todos")
print(resultado7)