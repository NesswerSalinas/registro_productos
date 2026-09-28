# Programa de Gestión de Inventario para "Sami la casa de las flores"
# Utiliza un diccionario para almacenar productos (clave: nombre, valor: [precio, stock])

def mostrar_menu():
    print("\n--- SISTEMA DE INVENTARIO: SAMI LA CASA DE LAS FLORES ---")
    print("1. Ver inventario de productos")
    print("2. Agregar un nuevo producto")
    print("3. Buscar un producto")
    print("4. Eliminar un producto")
    print("5. Salir")

def gestionar_inventario():
    # Diccionario inicial con algunos productos de la florería
    inventario = {
        "Rosas eternas rojas": [25.00, 10],
        "Caja luxury con chocolates": [35.00, 5],
        "Marco 3D personalizado": [20.00, 8],
        "Ramo de girasoles": [30.00, 6]
    }

    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-5): ")

        if opcion == "1":
            print("\n--- INVENTARIO ACTUAL ---")
            if not inventario:
                print("El inventario está vacío.")
            else:
                for producto, datos in inventario.items():
                    print(f"- {producto}: Precio: ${datos[0]:.2f} | Stock: {datos[1]} unidades")

        elif opcion == "2":
            print("\n--- AGREGAR NUEVO PRODUCTO ---")
            nuevo_producto = input("Ingresa el nombre del arreglo o regalo: ").strip()
            if nuevo_producto in inventario:
                print("¡Este producto ya existe en el inventario!")
            else:
                try:
                    precio = float(input("Ingresa el precio ($): "))
                    stock = int(input("Ingresa la cantidad en stock: "))
                    inventario[nuevo_producto] = [precio, stock]
                    print(f"¡Éxito! '{nuevo_producto}' ha sido agregado.")
                except ValueError:
                    print("Error: Por favor ingresa valores numéricos válidos para el precio y stock.")

        elif opcion == "3":
            print("\n--- BUSCAR PRODUCTO ---")
            busqueda = input("Ingresa el nombre del producto a buscar: ").strip()
            encontrado = False
            for producto, datos in inventario.items():
                if busqueda.lower() in producto.lower():
                    print(f"Encontrado -> {producto}: Precio: ${datos[0]:.2f} | Stock: {datos[1]} unidades")
                    encontrado = True
            if not encontrado:
                print("No se encontró ningún producto con ese nombre.")

        elif opcion == "4":
            print("\n--- ELIMINAR PRODUCTO ---")
            a_eliminar = input("Ingresa el nombre exacto del producto a eliminar: ").strip()
            if a_eliminar in inventario:
                del inventario[a_eliminar]
                print(f"El producto '{a_eliminar}' ha sido eliminado del inventario.")
            else:
                print("El producto no existe en el registro.")

        elif opcion == "5":
            print("\nSaliendo del sistema de inventario. ¡Gracias por usar el programa!")
            break
        else:
            print("Opción no válida. Por favor elige un número entre 1 y 5.")

# Ejecutar el programa
if __name__ == "__main__":
    gestionar_inventario()