class Usuario:
    nombre_banco = "Primer Dojo Nacional" 

    def __init__(self , name, email_address): 
        self.name = name
        self.email = email_address
        self.balance_cuenta = 0 

    def hacer_depósito(self, depósito): 
        self.balance_cuenta += depósito 

        return self

    def hacer_retiro(self, retiro):
        if self.balance_cuenta >= retiro:
            self.balance_cuenta -= retiro
        else:
            print("Saldo insuficiente para realizar el retiro.")
        return self


    def mostrar_balance_usuario(self):  
        print(f"Saldo de {self.name}: ${self.balance_cuenta}")


    def transferir_dinero(self, other_user, transferir): 
        if self.balance_cuenta >= transferir:
            self.balance_cuenta -= transferir
            other_user.hacer_depósito(transferir)
            print(f"Transferencia exitosa de {self.name} a {other_user.name} de ${transferir}")
        else:
            print("Saldo insuficiente para realizar la transferencia.")

        return self
    
Javiera = Usuario("Javiera Del Solar", "javiera@python.com")
Alexis = Usuario("Alexis Muñoz", "alexis@python.com")
Ana = Usuario("Ana Reveco", "ana@python.com")

print(f"{Javiera.name}, {Javiera.email}")
print(f"{Alexis.name}, {Alexis.email}")
print(f"{Ana.name}, {Ana.email}")


Javiera.hacer_depósito(5000).hacer_depósito(3000).hacer_depósito(10000).hacer_retiro(4000).hacer_retiro(20000).mostrar_balance_usuario()
#print(Javiera.balance_cuenta)

Alexis.hacer_depósito(10000).hacer_depósito(30000).hacer_retiro(8000).hacer_retiro(2000).mostrar_balance_usuario()
#print(Alexis.balance_cuenta)

Ana.hacer_depósito(80000).hacer_retiro(20000).hacer_retiro(5000).hacer_retiro(10000).mostrar_balance_usuario()
#print(Ana.balance_cuenta)

# Transferir dinero de Alexis a Javiera
Alexis.transferir_dinero(Javiera, 1000)

Javiera.mostrar_balance_usuario()
Alexis.mostrar_balance_usuario()
Ana.mostrar_balance_usuario()


"""
Código anterior

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

"""
"""
# Realizar primer retiro
Javiera.hacer_retiro(4000)
Alexis.hacer_retiro(8000)
Ana.hacer_retiro(20000)

print(Javiera.balance_cuenta)
print(Alexis.balance_cuenta)
print(Ana.balance_cuenta)

print("----------")

# Realizar segundo retiro de las cuentas 
Alexis.hacer_retiro(2000)
Ana.hacer_retiro(5000)

print(Alexis.balance_cuenta)
print(Ana.balance_cuenta)

print("----------")

# Realizar tercer retiro de las cuentas
Javiera.hacer_retiro(20000)
Ana.hacer_retiro(10000)

print(Javiera.balance_cuenta)
print(Ana.balance_cuenta)

print("----------")

# Transferir dinero de Alexis a Javiera
Alexis.transferir_dinero(Javiera, 1000)

print("----------")

Javiera.mostrar_balance_usuario()
Alexis.mostrar_balance_usuario()
Ana.mostrar_balance_usuario()

"""

