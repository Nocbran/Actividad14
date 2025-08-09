participantes = []
def AgregarParticipantes():
    while True:
        dorsal = input("Ingrese el numero de dorsal: ")

        nombre = input("Ingrese el nombre completo: ")
        edad = input("Ingrese la edad: ")
        categoria = input("Ingrese la categoria (Juvenil,Adulto,Master): ")

        participantes.append({
            'dorsal' : dorsal,
            'nombre' : nombre,
            'edad' : edad,
            'categoria' : categoria
        })

print("*******MENU DE OPCIONES*******")
print("1. Agregar participante")
print("2.Mostrar participantes ordenados por nombre")
print("Mostrar participantes ordenados por edad")
print("Salir")

opcion = input("Seleccione una opcion")