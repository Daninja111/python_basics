from pathlib import Path

base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada Familia.txt"))
guia2 = guia.with_name("La_Pedrera.txt") #va a otro archivo de la misma dire arriba
print(guia.parent) #Devuelve carpeta mas contigua a archivo puede ir mas atras +
print(base)
print(guia)
print(guia2)

guia = Path(Path.home(), "Europa")

for txt in Path(guia).glob("*.txt") #Muestra archivos txt de esa carpeta, todos (**/*.txt)
    print(txt)

guia = Path("Europa","españa","Barcelona","Sagrada_Familia.txt")
en_europa = guia.relative_top(Path("Europa"))
en_espania = guia.relative_top(Path("Europa", "España"))
print(en_europa) #Muestra fragmento de la direccion despues de la mencionada