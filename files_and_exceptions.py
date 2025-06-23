def read_file_to_dict(nombre_archivo):
    ventas_por_producto = {}
    try:
        with open(nombre_archivo, 'r') as archivo:
            linea = archivo.readline().strip()
            ventas = linea.split(';')
            for venta in ventas:
                if ':' in venta:
                    producto, valor = venta.split(':')
                    try:
                        monto = float(valor)
                        if producto in ventas_por_producto:
                            ventas_por_producto[producto].append(monto)
                        else:
                            ventas_por_producto[producto] = [monto]
                    except ValueError:
                        print(f"Valor inválido para el producto '{producto}': '{valor}'")
        return ventas_por_producto
    except FileNotFoundError:
        print(f"No se encontró el archivo '{nombre_archivo}'.")
        return {}

def process_dict(diccionario_ventas):
    for producto, montos in diccionario_ventas.items():
        total = sum(montos)
        promedio = total / len(montos) if montos else 0
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")

