import math


class Circulo:

    def __init__(self, radio: float):
        self.__radio = radio

    def calcular_area(self) -> float:
        return math.pi * math.pow(self.__radio, 2)

    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self.__radio


class Rectangulo:

    def __init__(self, base: float, altura: float):
        self.__base = base
        self.__altura = altura

    def calcular_area(self) -> float:
        return self.__base * self.__altura

    def calcular_perimetro(self) -> float:
        return (2 * self.__base) + (2 * self.__altura)


class Cuadrado:

    def __init__(self, lado: float):
        self.__lado = lado

    def calcular_area(self) -> float:
        return self.__lado * self.__lado

    def calcular_perimetro(self) -> float:
        return 4 * self.__lado


class TrianguloRectangulo:
    def __init__(self, base: float, altura: float):
        self.__base = base
        self.__altura = altura

    def calcular_area(self) -> float:
        return self.__base * self.__altura / 2

    def calcular_perimetro(self) -> float:

        return self.__base + self.__altura + self.calcular_hipotenusa()

    def calcular_hipotenusa(self) -> float:

        return math.pow(self.__base ** 2 + self.__altura ** 2, 0.5)

    def determinar_tipo_triangulo(self) -> str:

        hipotenusa = self.calcular_hipotenusa()
        if self.__base == self.__altura == hipotenusa:
            return "Equilátero"
        elif (self.__base != self.__altura and self.__base != hipotenusa
              and self.__altura != hipotenusa):
            return "Escaleno"
        else:
            return "Isósceles"


class PruebaFiguras:

    @staticmethod
    def main() -> None:
        figura1 = Circulo(2)
        figura2 = Rectangulo(1, 2)
        figura3 = Cuadrado(3)
        figura4 = TrianguloRectangulo(3, 5)
        figura5 = TrianguloRectangulo(4, 4)

        print("El área del círculo es =", figura1.calcular_area())
        print("El perímetro del círculo es =", figura1.calcular_perimetro())
        print()
        print("El área del rectángulo es =", figura2.calcular_area())
        print("El perímetro del rectángulo es =",
              figura2.calcular_perimetro())
        print()
        print("El área del cuadrado es =", figura3.calcular_area())
        print("El perímetro del cuadrado es =", figura3.calcular_perimetro())
        print()
        print("El área del triángulo es =", figura4.calcular_area())
        print("El perímetro del triángulo es =",
              figura4.calcular_perimetro())
        print("La hipotenusa del triángulo es =",
              figura4.calcular_hipotenusa())
        print("Es un triángulo", figura4.determinar_tipo_triangulo())
        print()
        print("Segundo triángulo (base 4, altura 4):")
        print("Es un triángulo", figura5.determinar_tipo_triangulo())


if __name__ == "__main__":
    PruebaFiguras.main()