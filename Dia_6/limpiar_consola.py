import subprocess

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
subprocess.call('cls', shell=True) #En caso de ocupar windows
print(f"Tu nombre es {nombre} y tienes {edad} años")

