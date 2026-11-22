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

        if opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Funcion en desarrollo.")


if __name__ == "__main__":
    main()
