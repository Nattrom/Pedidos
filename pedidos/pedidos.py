def crear_pedido(pedidos, pedido_id, cliente_id, producto_id, cantidad, clientes, productos):
    if pedido_id in pedidos:
        return pedidos, "Error: ID de pedido ya existe"

    if cliente_id not in clientes:
        return pedidos, "Error: Cliente no existe"

    if producto_id not in productos:
        return pedidos, "Error: Producto no existe"

    if cantidad <= 0:
        return pedidos, "Error: Cantidad inválida"

    precio = productos[producto_id][2]
    total = precio * cantidad

    pedidos[pedido_id] = (cliente_id, producto_id, cantidad, total)

    return pedidos, "\nPedido creado correctamente"


def consultar_pedidos(pedidos, clientes, productos):
    if not pedidos:
        return "\nNo hay pedidos registrados"

    resultado = ""

    for pedido_id in pedidos:
        cliente_id, producto_id, cantidad, total = pedidos[pedido_id]
        resultado += f"\nPedido {pedido_id}"
        resultado += f"\nCliente: {clientes[cliente_id][0]}"
        resultado += f"\nProducto: {productos[producto_id][1]}"
        resultado += f"\nCantidad: {cantidad}"
        resultado += f"\nTotal: {total}\n"

    return resultado


def calcular_ingresos(pedidos):
    total = 0
    for pedido_id in pedidos:
        total += pedidos[pedido_id][3]
    return total


def generar_reporte(pedidos, clientes, productos):
    if not pedidos:
        return "No hay datos para generar reporte"

    total_pedidos = len(pedidos)
    total_ingresos = calcular_ingresos(pedidos)

    reporte = "\n----- REPORTE FINAL -----"
    reporte += f"\nTotal pedidos: {total_pedidos}"
    reporte += f"\nTotal ingresos: {total_ingresos}"

    return reporte