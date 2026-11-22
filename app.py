
# Gestor de Tareas CLI
# Fase 3 - Integracion de funcionalidades

tareas = []


def agregar_tarea():
    titulo = input("Ingrese el titulo de la tarea: ")

    nueva_tarea = {
        "titulo": titulo,
        "completada": False
    }

    tareas.append(nueva_tarea)
    print("Tarea agregada correctamente.")


def listar_tareas():
    print("\n===== LISTA DE TAREAS =====")

    if not tareas:
        print("No hay tareas registradas.")
        return

    for i, tarea in enumerate(tareas, 1):
        estado = (
            "Completada"
            if tarea["completada"]
            else "Pendiente"
        )

        print(f"{i}. {tarea['titulo']} - {estado}")


def completar_tarea():
    print("\n===== COMPLETAR TAREA =====")

    if not tareas:
        print("No hay tareas registradas.")
        return

    listar_tareas()

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

    if not tareas:
        print("No hay tareas registradas.")
        return

    listar_tareas()

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
    print("\n===== SISTEMA DE GESTION DE TAREAS =====")
    print("Seleccione una opcion del menu:")
    print("1. Agregar nueva tarea")
    print("2. Consultar lista de tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea registrada")
    print("5. Salir del sistema")


def main():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_tarea()

        elif opcion == "2":
            listar_tareas()

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
