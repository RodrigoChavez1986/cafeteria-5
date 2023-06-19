from product_dao import ProductDAO


def mostrar_banner():
    print("*********************************")
    print("*                               *")
    print("*    Bienvenido a Cafetería 404 *")
    print("*                               *")
    print("*********************************")


def mostrar_menu():
    print("\n----------- MENÚ -----------")
    print("1. Realizar pedido")
    print("2. Acerca de")
    print("3. Salir")


def realizar_pedido():
    print("Realizando pedido...\n")

    # Obtener la lista de productos desde la base de datos
    lista_productos = ProductDAO.seleccionar()

    # Mostrar los productos disponibles
    print("Productos disponibles:")
    for i, producto in enumerate(lista_productos, start=1):
        print(f"{i}. {producto.nombre} - ${producto.precio}")

    pedido = []  # Lista para almacenar los productos del pedido

    while True:
        # Solicitar al usuario que elija un producto
        seleccion = int(
            input("\nSelecciona el número de producto que deseas ordenar (9 para salir): "))
        if seleccion == 9:
            break  # El usuario ha elegido salir del programa

        if seleccion < 1 or seleccion > len(lista_productos):
            print("Selección inválida.")
            continue

        producto_seleccionado = lista_productos[seleccion - 1]
        print(
            f"\nHas seleccionado: {producto_seleccionado.nombre} - ${producto_seleccionado.precio}\n")

        # Solicitar al usuario que ingrese la cantidad
        cantidad = int(input("Ingresa la cantidad: "))
        if cantidad <= 0:
            print("Cantidad inválida.")
            continue

        # Agregar el producto y la cantidad al pedido
        pedido.append((producto_seleccionado, cantidad))

    # Mostrar el resumen del pedido
    if pedido:
        print("\nResumen del pedido:")
        total = 0
        for producto, cantidad in pedido:
            subtotal = producto.precio * cantidad
            total += subtotal
            print(
                f"{producto.nombre} - ${producto.precio} x {cantidad} = ${subtotal}")

        print(f"\nTotal a pagar: ${total}")

        # Solicitar al usuario que ingrese la cantidad con la que pagará
        pago = float(input("\nIngrese la cantidad con la que pagará: "))
        if pago < total:
            print("El monto ingresado es insuficiente.")
        else:
            cambio = pago - total
            print(f"Cambio a devolver: ${cambio}")
    else:
        print("No se agregaron productos al pedido.")


def acerca_de():

    nombres = "Ahumada, Brian; Alancay, Abel Matías; Alsina, Maximiliano; Berrini, Alejandro; Calle, Sonia; Chávez, Rodrigo; Costa, María Eugenia; Romani, Santiago; Navarro, Lucas; Sanguinetti, Pablo"
    print("Lista de nombres:")
    print(nombres)


def salir():
    print("¡Hasta luego!")
    exit()


def main():
    mostrar_banner()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            realizar_pedido()
        elif opcion == "2":
            acerca_de()
        elif opcion == "3":
            salir()
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.\n")


if __name__ == '__main__':
    main()
