from enum import Enum


class TipoPlaneta(Enum):
    GASEOSO = 1
    TERRESTRE = 2
    ENANO = 3


class Planeta:
    UA_KM = 149_597_870
    LIMITE_CINTURON_UA = 3.4

    def __init__(self, nombre: str = None, cantidad_satelites: int = 0,
                 masa: float = 0.0, volumen: float = 0.0, diametro: int = 0,
                 distancia_sol: int = 0, tipo: TipoPlaneta = None,
                 es_observable: bool = False):
        self.__nombre = nombre
        self.__cantidad_satelites = cantidad_satelites
        self.__masa = masa                   
        self.__volumen = volumen             
        self.__diametro = diametro           
        self.__distancia_sol = distancia_sol 
        self.__tipo = tipo
        self.__es_observable = es_observable

    def imprimir(self) -> None:
        """Imprime en pantalla los valores de los atributos del planeta."""
        print("Nombre del planeta =", self.__nombre)
        print("Cantidad de satélites =", self.__cantidad_satelites)
        print("Masa del planeta =", self.__masa, "kg")
        print("Volumen del planeta =", self.__volumen, "km³")
        print("Diámetro del planeta =", self.__diametro, "km")
        print("Distancia al Sol =", self.__distancia_sol, "km")
        print("Tipo de planeta =", self.__tipo.name if self.__tipo else None)
        print("Es observable =", self.__es_observable)

    def calcular_densidad(self) -> float:
        """Devuelve la densidad del planeta: masa / volumen."""
        if self.__volumen == 0:
            return 0.0
        return self.__masa / self.__volumen

    def es_planeta_exterior(self) -> bool:
        limite = Planeta.UA_KM * Planeta.LIMITE_CINTURON_UA
        return self.__distancia_sol > limite


if __name__ == "__main__":
    p1 = Planeta("Tierra", 1, 5.9736e24, 1.08321e12, 12742,
                 150_000_000, TipoPlaneta.TERRESTRE, True)
    p1.imprimir()
    print("Densidad del planeta =", p1.calcular_densidad(), "kg/km³")
    print("Es planeta exterior =", p1.es_planeta_exterior())
    print()

    p2 = Planeta("Júpiter", 79, 1.899e27, 1.4313e15, 139820,
                 750_000_000, TipoPlaneta.GASEOSO, True)
    p2.imprimir()
    print("Densidad del planeta =", p2.calcular_densidad(), "kg/km³")
    print("Es planeta exterior =", p2.es_planeta_exterior())