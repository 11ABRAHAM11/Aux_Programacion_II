clientes = []
productos = []
ventas = []

def registrar_cliente():
    cid = input("ID Cliente: ")
    nombre = input("Nombre: ")
    clientes.append({"id": cid, "nombre": nombre})

def registrar_producto():
    pid = input("ID Producto: ")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))
    productos.append({"id": pid, "nombre": nombre, "precio": precio, "stock": stock})

def buscar_cliente(cid):
    for c in clientes:
        if c["id"] == cid:
            return c
    return None

def buscar_producto(pid):
    for p in productos:
        if p["id"] == pid:
            return p
    return None

def realizar_venta():
    cid = input("ID Cliente: ")
    cliente = buscar_cliente(cid)

    if not cliente:
        print("Cliente no existe")
        return

    pid = input("ID Producto: ")
    producto = buscar_producto(pid)

    if not producto or producto["stock"] <= 0:
        print("Producto no disponible")
        return

    cantidad = int(input("Cantidad: "))

    if cantidad > producto["stock"]:
        print("Stock insuficiente")
        return

    total = cantidad * producto["precio"]
    producto["stock"] -= cantidad

    ventas.append({
        "cliente": cliente["nombre"],
        "producto": producto["nombre"],
        "cantidad": cantidad,
        "total": total
    })

    print("Venta realizada. Total:", total)

def mostrar_ventas():
    for v in ventas:
        print(v)


while True:
    print("\n1. Registrar cliente")
    print("2. Registrar producto")
    print("3. Realizar venta")
    print("4. Mostrar ventas")
    print("0. Salir")

    op = input("Opción: ")

    if op == "1":
        registrar_cliente()
    elif op == "2":
        registrar_producto()
    elif op == "3":
        realizar_venta()
    elif op == "4":
        mostrar_ventas()
    elif op == "0":
        break
