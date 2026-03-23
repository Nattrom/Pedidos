def registrar_producto(productos, producto_id, nombre, precio):
    if producto_id in productos:
        return productos, "Error: ID de producto ya existe"

    productos[producto_id] = (producto_id, nombre, precio)
    return productos, "Producto registrado correctamente"