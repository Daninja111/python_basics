'''serie = 'N-02'

if serie == 'N-01':
    print("samsung")
elif serie == 'N-02':
    print("nokia")
elif serie == 'N-02':
    print("motorola")
else:
    print("No existe ese producto")'''
serie = 'N-02'
match serie:
    case 'N-01':
        print("samsung")
    case 'N-02':
        print("nokia")
    case 'N-03':
        print("motorola")
    case _:
        print("No existe ese producto")

cliente = {'nombre': 'Federico',
           'edad':34,
           'ocupacion': 'instructor'}
pelicula = {'titulo': 'Matrix',
            'ficha_tec':{'protagonista': 'keanu reeves',
                         'director':'Lana y Lilly Wachowski'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion':ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {'titulo': titulo,
            'ficha_tec':{'protagonista': protagonista,
                         'director': director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No se que es este elemento")