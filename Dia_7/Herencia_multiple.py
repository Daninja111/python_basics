class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('ja ja ja')

class Hijo(Padre, Madre): #El orden de llamamiento afecta mro
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.hablar()
mi_nieto.reir()