#Te permite acceder a la info mediante las claves
mi_dic = {'a1':'valor1', 'a2':'valor2'}
print(type(mi_dic))

resultado = mi_dic['a1']
print(resultado)

cliente = {'nombre':'pepita','apellido':'Palitos','peso':56,'talla':149}
print(cliente['apellido'])

mi_dic2 = {'c1':['a','b','c'],'c2':['d','e','f']}
print(mi_dic2['c2'][1].upper())

mi_dic3 = {1:'a',2:'b'}
mi_dic3[3] = 'c' #se crea una nueva clave, tb se puede reemplazar una

print(mi_dic3)
print(mi_dic.keys())
print(mi_dic.values())
print(mi_dic.items()) #muestra las tuplas

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])