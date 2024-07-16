
import random


trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
    "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]

sueldos = []


def asignar_sueldo_ale():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in trabajadores]
    print("sueldos se asigno con exito\n")

def clasificar_sueldos():
    menor = []

    medio = []

    mayor = []

    for i, sueldo in (sueldos):
        if sueldo < 800000:
            menor.append((trabajadores[i], sueldo))
        elif 800000 <= sueldo <= 2000000:
            medio.append((trabajadores[i], sueldo))
        else:
            mayor.append((trabajadores[i], sueldo))

    print("Sueldos menores a 800.000:", len(menor))
    for nombre, sueldo in menor:
        print(f"{nombre} ${sueldo}")

    print("\nSueldos entre $800.000 , $2.000.000:", len(medio))
    for nombre, sueldo in medio:
        print(f"{nombre} ${sueldo}")

    print("\nSueldos mayores a $2.000.000:", len(mayor))
    for nombre, sueldo in mayor:
        print(f"{nombre} ${sueldo}")

    print("\ntotal sueldo:", sum(sueldos), "\n")






def main():
    while True:
        print("Seleccione una opcion:")
        print("1.asignar sueldos aleatorios")
        print("2.clasificar sueldo")
        print("3.ver estadisticas")
        print("4.reporte de sueldos")
        print("6.salir del programa")

        opcion = input("Ingrese el numero de la opcion: ")

        if opcion == "1":
            asignar_sueldo_ale()
        elif opcion == "2":
            clasificar_sueldos()
        elif opcion == "3":
            print("fin programa")
            print("rut 20.136.460-4")
            break
        else:
            print("Opcion no valida, reintentar: xd lol .\n")


main()