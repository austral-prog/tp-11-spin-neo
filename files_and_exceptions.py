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
                        print(f"⚠️ No se pudo convertir el valor '{valor}' a float para el producto '{producto}'")
        return ventas_por_producto
    except FileNotFoundError:
        print(f"❌ El archivo '{nombre_archivo}' no fue encontrado.")
        return {}
