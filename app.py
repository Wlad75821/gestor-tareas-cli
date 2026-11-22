
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
