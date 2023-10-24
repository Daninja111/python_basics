class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
    #Construye lo que realiza el metodo string
    def __str__(self):
        return f'ALbum: {self.titulo} de {self.autor}'
    def __len__(self):
        return self.canciones
    def __del__(self):
        print('Se ha eliminado el cd')

mi_cd = CD('Pink FLoyd', 'The wall', 24)

print(str(mi_cd))

del mi_cd #Elimina la instancia creada