
class Usuario:
    nombre_banco = "Primer Dojo Nacional" # los atributos de clase se definen en la clase

    def __init__(self , name, email_address): # ¡ahora nuestro método tiene 2 parámetros!
        self.name = name
        self.email = email_address
        self.balance_cuenta = 0 # el balance de la cuenta se establece en $0

    # agregando el método de depósito
    def hacer_depósito(self, depósito): # toma un argumento que es el monto del depósito
        self.balance_cuenta += depósito # la cuenta del usuario específico aumenta en la cantidad del valor recibido

    def hacer_retiro(self, retiro):
        if self.balance_cuenta >= retiro:
            self.balance_cuenta -= retiro
        else:
            print("Saldo insuficiente para realizar el retiro.")

    def mostrar_balance_usuario(self):  # Saldo total de las cuentas de cada usuario
        print(f"Saldo de {self.name}: ${self.balance_cuenta}")

    def transferir_dinero(self, other_user, transferir): #Trasferir dinero
        if self.balance_cuenta >= transferir:
            self.balance_cuenta -= transferir
            other_user.hacer_depósito(transferir)
            print(f"Transferencia exitosa de {self.name} a {other_user.name} de ${transferir}")
        else:
            print("Saldo insuficiente para realizar la transferencia.")
    
# Crear instancias de usuarios
Javiera = Usuario("Javiera Del Solar", "javiera@python.com")
Alexis = Usuario("Alexis Muñoz", "alexis@python.com")
Ana = Usuario("Ana Reveco", "ana@python.com")

print(f"{Javiera.name}, {Javiera.email}")
print(f"{Alexis.name}, {Alexis.email}")
print(f"{Ana.name}, {Ana.email}")

# Realizar Depósitos
Javiera.hacer_depósito(5000)
Javiera.hacer_depósito(3000)
Javiera.hacer_depósito(10000)
Alexis.hacer_depósito(10000)
Alexis.hacer_depósito(30000)
Ana.hacer_depósito(80000)

# Imprimir saldos de cuenta de depósito
print(Javiera.balance_cuenta)
print(Alexis.balance_cuenta)
print(Ana.balance_cuenta)

print("----------")

# Realizar primer retiro
Javiera.hacer_retiro(4000)
Alexis.hacer_retiro(8000)
Ana.hacer_retiro(20000)


# Imprimir saldos del primer retiro de las cuentas
print(Javiera.balance_cuenta)
print(Alexis.balance_cuenta)
print(Ana.balance_cuenta)

print("----------")

# Realizar segundo retiro de las cuentas 
Alexis.hacer_retiro(2000)
Ana.hacer_retiro(5000)

# Imprimir saldos de segundo retiro de las cuentas
print(Alexis.balance_cuenta)
print(Ana.balance_cuenta)

print("----------")

# Realizar tercer retiro de las cuentas
Javiera.hacer_retiro(20000)
Ana.hacer_retiro(10000)

# Imprimir tercer retiro de las cuentas
print(Javiera.balance_cuenta)
print(Ana.balance_cuenta)

print("----------")

# Transferir dinero de Alexis a Javiera
Alexis.transferir_dinero(Javiera, 1000)

print("----------")

# Mostrar saldos de cuenta
Javiera.mostrar_balance_usuario()
Alexis.mostrar_balance_usuario()
Ana.mostrar_balance_usuario()



