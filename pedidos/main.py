from clientes import registrar_cliente
from productos import registrar_producto
from pedidos import crear_pedido, consultar_pedidos, calcular_ingresos, generar_reporte
from visual import limpiar, animacion, pausa, titulo, mostrar_menu


def menu():
    clientes = {}
    productos = {}
    pedidos = {}

    while True:
        titulo()
        mostrar_menu()

        try:
            opcion = int(input("\nSeleccione una opción: "))
            limpiar()
        except:
            animacion("Error: Debe ingresar un número")
            pausa()
            continue

        if opcion == 1:
            while True:
                try:
                    cid = int(input("ID cliente: "))
                    nombre = input("Nombre: ")
                    correo = input("Correo: ")

                    clientes, msg = registrar_cliente(clientes, cid, nombre, correo)
                    animacion(msg)

                    otro = input("¿Agregar otro cliente? (s/n): ").lower()
                    if otro != "s":
                        break
                except:
                    animacion("Error en datos")

            pausa()

        elif opcion == 2:
            while True:
                try:
                    pid = int(input("ID producto: "))
                    nombre = input("Nombre: ")
                    precio = float(input("Precio: "))

                    productos, msg = registrar_producto(productos, pid, nombre, precio)
                    animacion(msg)

                    otro = input("¿Agregar otro producto? (s/n): ").lower()
                    if otro != "s":
                        break
                except:
                    animacion("Error en datos")

            pausa()

        elif opcion == 3:
            while True:
                try:
                    peid = int(input("ID pedido: "))
                    cid = int(input("ID cliente: "))
                    pid = int(input("ID producto: "))
                    cant = int(input("Cantidad: "))

                    pedidos, msg = crear_pedido(pedidos, peid, cid, pid, cant, clientes, productos)
                    animacion(msg)

                    otro = input("¿Agregar otro pedido? (s/n): ").lower()
                    if otro != "s":
                        break
                except:
                    animacion("Error en datos")

            pausa()

        elif opcion == 4:
            print(consultar_pedidos(pedidos, clientes, productos))
            pausa()

        elif opcion == 5:
            print("Ingresos totales:", calcular_ingresos(pedidos))
            pausa()

        elif opcion == 6:
            print(generar_reporte(pedidos, clientes, productos))
            pausa()

        elif opcion == 7:
            animacion("Saliendo del sistema...", 0.08)
            break

        else:
            animacion("Opción inválida")
            pausa()


menu()