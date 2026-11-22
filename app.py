
# Gestor de Tareas CLI
# Fase 2 - Operaciones Basicas

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
            agregar_tarea()

        elif opcion == "2":
            listar_tareas()

        elif opcion == "3":
            print("Funcion en desarrollo.")

        elif opcion == "4":
            print("Funcion en desarrollo.")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    main()
