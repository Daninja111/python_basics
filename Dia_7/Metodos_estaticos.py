class Pajaro:
    alas = True
    #metodo constructor al atributo se le asigna parametro
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    def piar(self):
        print(f'pio, mi color es {self.color}')
    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros')
        self.piar()
    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora nuestro pájaro es de color {self.color}')

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)
#No puede ocupar atributos de instancia, solo de clase
    @staticmethod
    def mirar():
        print(f'El pájaro mira')
#Metodo que no permite modificar a los de instancia ni a los de clase
piolin = Pajaro('amarillo', 'canario')

#Los metodos de clase no necesitan de instancias para ejecutarse
Pajaro.mirar()