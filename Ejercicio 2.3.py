from enum import Enum


class TipoCombustible(Enum):
    GASOLINA = 1
    BIOETANOL = 2
    DIESEL = 3
    BIODIESEL = 4
    GAS_NATURAL = 5


class TipoAutomovil(Enum):
    CIUDAD = 1
    SUBCOMPACTO = 2
    COMPACTO = 3
    FAMILIAR = 4
    EJECUTIVO = 5
    SUV = 6


class TipoColor(Enum):
    BLANCO = 1
    NEGRO = 2
    ROJO = 3
    NARANJA = 4
    AMARILLO = 5
    VERDE = 6
    AZUL = 7
    VIOLETA = 8


class Automovil:

    def __init__(self, marca: str, modelo: int, motor: float,
                 tipo_combustible: TipoCombustible,
                 tipo_automovil: TipoAutomovil, numero_puertas: int,
                 cantidad_asientos: int, velocidad_maxima: int,
                 color: TipoColor):
        self.__marca = marca                        
        self.__modelo = modelo                      
        self.__motor = motor                        
        self.__tipo_combustible = tipo_combustible
        self.__tipo_automovil = tipo_automovil
        self.__numero_puertas = numero_puertas
        self.__cantidad_asientos = cantidad_asientos
        self.__velocidad_maxima = velocidad_maxima 
        self.__color = color
        self.__velocidad_actual = 0                 

    def get_marca(self) -> str:
        return self.__marca

    def get_modelo(self) -> int:
        return self.__modelo

    def get_motor(self) -> float:
        return self.__motor

    def get_tipo_combustible(self) -> TipoCombustible:
        return self.__tipo_combustible

    def get_tipo_automovil(self) -> TipoAutomovil:
        return self.__tipo_automovil

    def get_numero_puertas(self) -> int:
        return self.__numero_puertas

    def get_cantidad_asientos(self) -> int:
        return self.__cantidad_asientos

    def get_velocidad_maxima(self) -> int:
        return self.__velocidad_maxima

    def get_color(self) -> TipoColor:
        return self.__color

    def get_velocidad_actual(self) -> int:
        return self.__velocidad_actual


    def set_marca(self, marca: str) -> None:
        self.__marca = marca

    def set_modelo(self, modelo: int) -> None:
        self.__modelo = modelo

    def set_motor(self, motor: float) -> None:
        self.__motor = motor

    def set_tipo_combustible(self, tipo_combustible: TipoCombustible) -> None:
        self.__tipo_combustible = tipo_combustible

    def set_tipo_automovil(self, tipo_automovil: TipoAutomovil) -> None:
        self.__tipo_automovil = tipo_automovil

    def set_numero_puertas(self, numero_puertas: int) -> None:
        self.__numero_puertas = numero_puertas

    def set_cantidad_asientos(self, cantidad_asientos: int) -> None:
        self.__cantidad_asientos = cantidad_asientos

    def set_velocidad_maxima(self, velocidad_maxima: int) -> None:
        self.__velocidad_maxima = velocidad_maxima

    def set_color(self, color: TipoColor) -> None:
        self.__color = color

    def set_velocidad_actual(self, velocidad_actual: int) -> None:
        self.__velocidad_actual = velocidad_actual

    # ------------- Métodos de comportamiento -------------
    def acelerar(self, incremento_velocidad: int) -> None:

        nueva_velocidad = self.__velocidad_actual + incremento_velocidad
        if nueva_velocidad <= self.__velocidad_maxima:
            self.__velocidad_actual = nueva_velocidad
        else:
            print("No se puede incrementar a una velocidad superior "
                  "a la máxima del automóvil.")

    def desacelerar(self, decremento_velocidad: int) -> None:

        if self.__velocidad_actual - decremento_velocidad >= 0:
            self.__velocidad_actual -= decremento_velocidad
        else:
            print("No se puede decrementar a una velocidad negativa.")

    def frenar(self) -> None:

        self.__velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia: float) -> float:

        if self.__velocidad_actual == 0:
            print("El automóvil está detenido, no se puede calcular "
                  "el tiempo de llegada.")
            return 0.0
        return distancia / self.__velocidad_actual

    def imprimir(self) -> None:

        print("Marca =", self.__marca)
        print("Modelo =", self.__modelo)
        print("Motor =", self.__motor, "litros")
        print("Tipo de combustible =", self.__tipo_combustible.name)
        print("Tipo de automóvil =", self.__tipo_automovil.name)
        print("Número de puertas =", self.__numero_puertas)
        print("Cantidad de asientos =", self.__cantidad_asientos)
        print("Velocidad máxima =", self.__velocidad_maxima, "km/h")
        print("Color =", self.__color.name)



if __name__ == "__main__":
    auto1 = Automovil("Ford", 2018, 3.0, TipoCombustible.DIESEL,
                      TipoAutomovil.EJECUTIVO, 5, 6, 250, TipoColor.NEGRO)
    auto1.imprimir()
    print()

    auto1.set_velocidad_actual(100)
    print("Velocidad actual =", auto1.get_velocidad_actual())

    auto1.acelerar(20)
    print("Velocidad actual =", auto1.get_velocidad_actual())

    auto1.desacelerar(50)
    print("Velocidad actual =", auto1.get_velocidad_actual())

    print("Tiempo estimado para recorrer 140 km =",
          auto1.calcular_tiempo_llegada(140), "horas")

    auto1.frenar()
    print("Velocidad actual =", auto1.get_velocidad_actual())


    auto1.desacelerar(20)
    auto1.acelerar(300)