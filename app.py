
# Gestor de Tareas CLI
# Fase 2 - Operaciones Avanzadas

tareas = [
    {"titulo": "Estudiar Python", "completada": False},
    {"titulo": "Realizar practica de Git", "completada": False}
]


def completar_tarea():
    print("\n===== COMPLETAR TAREA =====")

    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea['titulo']}")

    try:
        numero = int(input("Numero de tarea a completar: "))

        if 1 <= numero <= len(tareas):
            tareas[numero - 1]["completada"] = True
            print("Tarea completada correctamente.")
        else:
            print("Numero de tarea no valido.")

    except ValueError:
        print("Debe ingresar un numero valido.")


def eliminar_tarea():
    print("\n===== ELIMINAR TAREA =====")

    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea['titulo']}")

    try:
        numero = int(input("Numero de tarea a eliminar: "))

        if 1 <= numero <= len(tareas):
            tarea = tareas.pop(numero - 1)
            print(f"Tarea '{tarea['titulo']}' eliminada.")
        else:
            print("Numero de tarea no valido.")

    except ValueError:
        print("Debe ingresar un numero valido.")


def mostrar_menu():
    print("\n===== GESTOR DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            print("Funcion en desarrollo.")

        elif opcion == "2":
            print("Funcion en desarrollo.")

        elif opcion == "3":
            completar_tarea()

        elif opcion == "4":
            eliminar_tarea()

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    main()
