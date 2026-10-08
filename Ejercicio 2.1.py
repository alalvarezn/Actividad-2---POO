
class Persona:

    def __init__(self, nombre: str, apellidos: str,
                 numero_documento_identidad: str, anio_nacimiento: int):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__numero_documento_identidad = numero_documento_identidad
        self.__anio_nacimiento = anio_nacimiento

    def imprimir(self) -> None:
        print("Nombre =", self.__nombre)
        print("Apellidos =", self.__apellidos)
        print("Número de documento de identidad =",
              self.__numero_documento_identidad)
        print("Año de nacimiento =", self.__anio_nacimiento)
        print()

if __name__ == "__main__":
    p1 = Persona("Pedro", "Pérez", "1053121010", 1998)
    p2 = Persona("Luis", "León", "1053223344", 2001)

    p1.imprimir()
    p2.imprimir()