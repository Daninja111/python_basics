#No permite elementos repetidos, si los hubiera los elimina auto.
# Inmutables, listas y dic no admitidos. SI admite tuplas

mi_set = set([4,5])
print(mi_set)

otro_set = {1,2,3}
#No se puede buscar por posicion
print(len(otro_set))
print(2 in mi_set)

s3 = mi_set.union(otro_set)
print(s3)

otro_set.add(7)
print(otro_set)
otro_set.remove(7) #discard hace lo mismo pero si no existe funciona
print(otro_set)

otro_set.clear()
print(otro_set)