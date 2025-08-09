class Participante:
    def __init__(self, dorsal, nombre, edad, categoria):
        self.dorsal = dorsal
        self.nombre = nombre
        self.edad = edad
        self.categoria = categoria

        class Carrera:
            def __init__(self):
                self.participantes = []


print("*******MENU DE OPCIONES*******")
print("1. Agregar participante")
print("2.Mostrar participantes ordenados por nombre")
print("Mostrar participantes ordenados por edad")
print("Salir")

opcion = input("Seleccione una opcion")