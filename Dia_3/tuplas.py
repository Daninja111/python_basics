#Las tuplas ocupan menos espacio y las usamos cuando no queremos que se modifiquen

mi_tuple = (1,2,2,4)
mi_tuple2 = (1,2.7,"tata")

print(mi_tuple[1])

x,y,z,t= mi_tuple
print(x)

print(mi_tuple.count(2))
print(mi_tuple.index(2))
