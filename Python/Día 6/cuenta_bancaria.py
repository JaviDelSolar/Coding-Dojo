
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
        print(f"Balance: {self.balance}")
        return self
    
    def generar_interés(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interés)
        return self
    
    @classmethod
    def imprimir_cuentas(cls):
        for account in cls.todas_las_cuentas:
            account.mostrar_info_cuenta()


Javiera = CuentaBancaria(1, 0)
Alexis = CuentaBancaria(2, 20000)

Javiera.depósito(40000).depósito(50000).depósito(10000).retiro(200000).mostrar_info_cuenta()
Alexis.depósito(50000).depósito(10000).retiro(1000).retiro(10000).retiro(4000).retiro(5000).mostrar_info_cuenta()

CuentaBancaria.imprimir_cuentas()

