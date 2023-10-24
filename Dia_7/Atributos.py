class Pajaro:
    alas = True
    #metodo constructor al atributo se le asigna parametro
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('negro', 'Tucan')

print(f'Mi pájaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}')
print(Pajaro.alas)