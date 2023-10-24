precios_cafe=[('Capuchino',1.5),('Expresso',1.2),('Moka',1.9)]

for cafe,precio in precios_cafe:
    print(cafe)

#Lo mismo pero hecho en función
def cafe_mas_caro(lista_precios):

    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro, precio_mayor)
print(cafe_mas_caro(precios_cafe))
cafe,precio = cafe_mas_caro(precios_cafe)
print(f"El café más caro es {cafe} ${precio}")