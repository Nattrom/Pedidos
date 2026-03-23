def registrar_cliente(clientes, cliente_id, nombre, correo):
    if cliente_id in clientes:
        return clientes, "\nError: ID de cliente ya existe"

    clientes[cliente_id] = (nombre, correo)
    return clientes, "\nCliente registrado correctamente"