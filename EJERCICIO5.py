from enum import Enum

class tipoCuenta(Enum):
    AHORROS = "AHORROS"
    CORRIENTE = "CORRIENTE"

class CuentaBancaria:
    def __init__(self, nombresTitular, apellidosTitular, numeroCuenta, tipoCuenta):
        self.nombresTitular = nombresTitular
        self.apellidosTitular = apellidosTitular
        self.numeroCuenta = numeroCuenta
        self.tipoCuenta = tipoCuenta
        self.saldo = 0
    
    def imprimir(self):
        print(f"Nombres del titular = {self.nombresTitular}")
        print(f"Apellidos del titular = {self.apellidosTitular}")
        print(f"Número de cuenta = {self.numeroCuenta}")
        print(f"Tipo de cuenta = {self.tipoCuenta.value}")
        print(f"Saldo = {float(self.saldo)}")
    
    def consultarSaldo(self):
        print(f"El saldo actual es = {self.saldo}")
    
    def consignar(self, valor):
        if (valor > 0):
            self.saldo = self.saldo + valor
            print(f"Se ha consignado ${valor} en la cuenta. El nuevo saldo es ${float(self.saldo)}")
            return True
        else:
            print("El valor a consignar debe ser mayor que cero")
            return False
    
    def retirar(self, valor):
        if ((valor > 0) and (valor <= self.saldo)):
            self.saldo = self.saldo - valor
                
            print(f"Se ha retirado ${valor} en la cuenta. El nuevo saldo es ${float(self.saldo)}")
            return True
        else:
            print(f"El valor a retirar debe ser menor que el saldo actual")
            return False
    
    def compararCuentas(self, cuenta2):
        if self.numeroCuenta == cuenta2.numeroCuenta:
            print("Las cuentas son iguales")
            return True
        else:
            print("Las cuentas son diferentes")
            return False
    
    def transferencia(self, cuenta, valor):
        if self.retirar(valor):
            cuenta.consignar(valor)
            print(f"Transferencia exitosa de ${valor} a la cuenta {cuenta.numeroCuenta}")
            return True
        else:
            print("Transferencia fallida")
            return False
        
cuenta1 = CuentaBancaria("Pedro", "Pérez", 123456789, tipoCuenta.AHORROS)
cuenta1.imprimir()
cuenta1.consignar(200000)
cuenta1.consignar(300000)
cuenta1.retirar(400000)
print()

cuenta2 = CuentaBancaria("Juan", "Gómez", 987654321, tipoCuenta.CORRIENTE)
cuenta1.compararCuentas(cuenta2)
cuenta1.transferencia(cuenta2, 50000)
