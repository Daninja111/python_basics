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
piolin = Pajaro('amarillo', 'canario')

piolin.pintar_negro()
piolin.volar(100)
piolin.alas = False

print(piolin.alas)