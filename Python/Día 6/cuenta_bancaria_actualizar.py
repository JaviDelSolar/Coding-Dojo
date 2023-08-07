
class CuentaBancaria:
    
    nombre_banco = "Primer Dojo Nacional" 
    todas_las_cuentas = []

    def __init__(self, tasa_interés, balance): 
        self.tasa_interés = tasa_interés
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)

    def depósito(self, amount):
        self.balance += amount
        return self
    

    def retiro(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Fondo insuficiente: cobrando una tarifa de $5")
            self.balance -= 5
        return self
        
    def mostrar_info_cuenta(self):
        return (self.balance)
        
    
    def generar_interés(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interés)
        return self
    
    @classmethod
    def imprimir_cuentas(cls):
        for account in cls.todas_las_cuentas:
            account.mostrar_info_cuenta()


class Usuario:
    nombre_banco = "Primer Dojo Nacional" 

    def __init__(self , name): 
        self.name = name
        self.cuenta = {
            "checking" : CuentaBancaria(.05,10000),
            "savings" : CuentaBancaria(.05,50000)
        }
        self.cuenta1 = {
            "checking" : CuentaBancaria(.05,5000),
            "savings" : CuentaBancaria(.05,100000)
        }

    def hacer_depósito(self, depósito): 
        self.balance_cuenta += depósito 

        return self

    def hacer_retiro(self, retiro):
        if self.balance_cuenta >= retiro:
            self.balance_cuenta -= retiro
        else:
            print("Saldo insuficiente para realizar el retiro.")
        return self


    def mostrar_balance_usuario1(self):  
        print(f"Saldo de {self.name}: Checking ${self.cuenta['checking'].mostrar_info_cuenta()}")
        print(f"Saldo de {self.name}: Savings ${self.cuenta['savings'].mostrar_info_cuenta()}")
        return self
    
    def mostrar_balance_usuario2(self):  
        print(f"Saldo de {self.name}: Checking ${self.cuenta1['checking'].mostrar_info_cuenta()}")
        print(f"Saldo de {self.name}: Savings ${self.cuenta1['savings'].mostrar_info_cuenta()}")
        return self

    def transferir_dinero(self, other_user, transferir): 
        if self.balance_cuenta >= transferir:
            self.balance_cuenta -= transferir
            other_user.hacer_depósito(transferir)
            print(f"Transferencia exitosa de {self.name} a {other_user.name} de ${transferir}")
        else:
            print("Saldo insuficiente para realizar la transferencia.")

        return self

Javiera = Usuario("Javiera Del Solar")
Alexis = Usuario("Alexis Muñoz")


Javiera.cuenta['checking'].depósito(1000).retiro(500)
Javiera.mostrar_balance_usuario1()
Alexis.cuenta1['checking'].depósito(1000).retiro(10000)
Alexis.mostrar_balance_usuario2()

