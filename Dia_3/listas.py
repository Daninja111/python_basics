mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
print(type(mi_lista))
print(len(mi_lista))
print(mi_lista[1])
print(mi_lista[0:2])
print(mi_lista+mi_lista2)

mi_lista[1] = 'abc'
print(mi_lista)
mi_lista2.append('lala')
print(mi_lista2)
mi_lista2.pop(0) #Sin argumento elimina el ultimo
print(mi_lista2) #se puede guardar en variable el elemento eliminado

lista = ['g', 'a', 'k', 'w']
lista.sort() #Es un metodo que no devuelve nada por lo tanto es None
print(lista)
lista.reverse()
print(lista)