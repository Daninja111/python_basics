from pathlib import Path, PureWindowsPath
carpeta = Path("C:/Users/mazzi/Documents/Python/Dia_6/Prueba.txt")
ruta_windows= PureWindowsPath(carpeta)
print(ruta_windows)
print(carpeta.read_text()) #Ya no se debe abrir ni cerrar
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)
if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe")