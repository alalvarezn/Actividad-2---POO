from enum import Enum


class TipoCuenta(Enum):
    AHORROS = 1
    CORRIENTE = 2


class CuentaBancaria:
    def __init__(self, nombres_titular: str, apellidos_titular: str,
                 numero_cuenta: int, tipo_cuenta: TipoCuenta):

        self.__nombres_titular = nombres_titular
        self.__apellidos_titular = apellidos_titular
        self.__numero_cuenta = numero_cuenta
        self.__tipo_cuenta = tipo_cuenta
        self.__saldo = 0.0

    def imprimir(self) -> None:

        print("Nombres del titular =", self.__nombres_titular)
        print("Apellidos del titular =", self.__apellidos_titular)
        print("Número de cuenta =", self.__numero_cuenta)
        print("Tipo de cuenta =", self.__tipo_cuenta.name)
        print("Saldo =", self.__saldo)

    def consultar_saldo(self) -> None:

        print("El saldo actual es =", self.__saldo)

    def consignar(self, valor: float) -> bool:

        if valor > 0:
            self.__saldo += valor
            print(f"Se ha consignado ${valor} en la cuenta. "
                  f"El nuevo saldo es ${self.__saldo}")
            return True
        print("El valor a consignar debe ser mayor que cero.")
        return False

    def retirar(self, valor: float) -> bool:
        if valor <= 0:
            print("El valor a retirar debe ser mayor que cero.")
            return False
        if valor > self.__saldo:
            print(f"No se puede retirar ${valor}: el valor supera "
                  f"el saldo actual (${self.__saldo}).")
            return False
        self.__saldo -= valor
        print(f"Se ha retirado ${valor} de la cuenta. "
              f"El nuevo saldo es ${self.__saldo}")
        return True


if __name__ == "__main__":
    cuenta = CuentaBancaria("Pedro", "Pérez", 123456789, TipoCuenta.AHORROS)
    cuenta.imprimir()
    print()

    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)
    cuenta.consultar_saldo()
    print()


    cuenta.retirar(500000)   
    cuenta.consignar(-1000)  
    cuenta.consultar_saldo()