def describir_persona(*nombre, **kwargs):
    for arg in nombre:
        print(f"Características de {arg}:")
    for clave,valor in kwargs.items():
        print(f"{clave}: {valor}")