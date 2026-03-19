#REGISTRO DE CLIENTES
hola mundo
def registrar_cliente(clientes, cliente_id, nombre, correo):
    if cliente_id in clientes:
        return clientes, "Error: ID de cliente ya existe"
    
    clientes[cliente_id] = (nombre, correo)
    return clientes, "Cliente registrado correctamente"

#REGISTRO DE PRODUCTOS

def registrar_producto(productos, producto_id, nombre, precio):
    if producto_id in productos:
        return productos, "Error: ID de producto ya existe"
    
    productos[producto_id] = (producto_id, nombre, precio)
    return productos, "Producto registrado correctamente"

# CREACIÓN DE PEDIDOS

def crear_pedido(pedidos, pedido_id, cliente_id, producto_id, cantidad, clientes, productos):
    if pedido_id in pedidos:
        return pedidos, "Error: ID de pedido ya existe"

    if cliente_id not in clientes:
        return pedidos, "Error: Cliente no existe"

    if producto_id not in productos:
        return pedidos, "Error: Producto no existe"

    if cantidad <= 0:
        return pedidos, "Error: Cantidad inválida"

    producto = productos[producto_id]
    precio = producto[2]
    total = precio * cantidad

    pedidos[pedido_id] = (cliente_id, producto_id, cantidad, total)

    return pedidos, "Pedido creado correctamente"

#CONSULTA DE PEDIDOS

def consultar_pedidos(pedidos, clientes, productos):
    if not pedidos:
        return "No hay pedidos registrados"

    resultado = ""
    
    for pedido_id in pedidos:
        cliente_id, producto_id, cantidad, total = pedidos[pedido_id]
        nombre_cliente = clientes[cliente_id][0]
        nombre_producto = productos[producto_id][1]

        resultado += f"\nPedido {pedido_id}\n"
        resultado += f"Cliente: {nombre_cliente}\n"
        resultado += f"Producto: {nombre_producto}\n"
        resultado += f"Cantidad: {cantidad}\n"
        resultado += f"Total: {total}\n"

    return resultado

#CÁLCULO DE INGRESOS

def calcular_ingresos(pedidos):
    total = 0

    for pedido_id in pedidos:
        total += pedidos[pedido_id][3]

    return total

#REPORTE FINAL

def generar_reporte(pedidos, clientes, productos):
    if not pedidos:
        return "No hay datos para generar reporte"

    total_pedidos = len(pedidos)
    total_ingresos = calcular_ingresos(pedidos)

    pedidos_por_cliente = {}
    productos_vendidos = {}

    for pedido_id in pedidos:
        cliente_id, producto_id, cantidad, _ = pedidos[pedido_id]

        # Contar pedidos por cliente
        if cliente_id in pedidos_por_cliente:
            pedidos_por_cliente[cliente_id] += 1
        else:
            pedidos_por_cliente[cliente_id] = 1

        # Contar productos vendidos
        if producto_id in productos_vendidos:
            productos_vendidos[producto_id] += cantidad
        else:
            productos_vendidos[producto_id] = cantidad

    reporte = "\n----- REPORTE FINAL -----\n"
    reporte += f"Total pedidos: {total_pedidos}\n"
    reporte += f"Total ingresos: {total_ingresos}\n"

    reporte += "\nPedidos por cliente:\n"
    for cliente_id in pedidos_por_cliente:
        reporte += f"{clientes[cliente_id][0]}: {pedidos_por_cliente[cliente_id]}\n"

    reporte += "\nProductos vendidos:\n"
    for producto_id in productos_vendidos:
        reporte += f"{productos[producto_id][1]}: {productos_vendidos[producto_id]}\n"

    return reporte
# MENÚ INTERACTIVO
def menu():
    clientes = {}
    productos = {}
    pedidos = {}

    opcion = 0

    while opcion != 7:
        print("\n====== MENÚ SISTEMA DE PEDIDOS ======")
        print("1. Registrar cliente")
        print("2. Registrar producto")
        print("3. Crear pedido")
        print("4. Ver pedidos")
        print("5. Ver ingresos")
        print("6. Reporte final")
        print("7. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except:
            print("Error: Debe ingresar un número")
            continue

        if opcion == 1:
            try:
                cid = int(input("ID cliente: "))
                nombre = input("Nombre: ")
                correo = input("Correo: ")
                clientes, msg = registrar_cliente(clientes, cid, nombre, correo)
                print(msg)
            except:
                print("Error en datos de entrada")

        elif opcion == 2:
            try:
                pid = int(input("ID producto: "))
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                productos, msg = registrar_producto(productos, pid, nombre, precio)
                print(msg)
            except:
                print("Error en datos de entrada")

        elif opcion == 3:
            try:
                peid = int(input("ID pedido: "))
                cid = int(input("ID cliente: "))
                pid = int(input("ID producto: "))
                cant = int(input("Cantidad: "))
                pedidos, msg = crear_pedido(pedidos, peid, cid, pid, cant, clientes, productos)
                print(msg)
            except:
                print("Error en datos de entrada")

        elif opcion == 4:
            print(consultar_pedidos(pedidos, clientes, productos))

        elif opcion == 5:
            print("Ingresos totales:", calcular_ingresos(pedidos))

        elif opcion == 6:
            print(generar_reporte(pedidos, clientes, productos))

        elif opcion == 7:
            print("Saliendo del sistema...")

        else:
            print("Opción inválida")

    return clientes, productos, pedidos
# EJECUCIÓN
menu()
