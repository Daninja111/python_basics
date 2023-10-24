class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
class Cliente(Persona):
    def __init__(self, nombre, apellido, num_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.balance= balance
    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido} /n Tu saldo es: $ {self.balance}'
    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Deposito aceptado")
    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")


#Funciones
def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    num_cuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cl, apellido_cl, num_cuenta)
    return cliente
def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print('Elige: Depositar (D), Retirar (R), o Salir (R)')
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_dep)
        if opcion == 'R':
            monto_ret = int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)
    print("Gracias por operar con nosotros")

inicio()



