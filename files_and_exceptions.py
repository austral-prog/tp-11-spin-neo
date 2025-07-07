def read_file_to_dict(filename):
    ventas_por_producto = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            linea = file.readline().strip()
            ventas = linea.split(';')

            for venta in ventas:
                if venta:
                    try:
                        producto, valor = venta.split(':')
                        valor = float(valor)
                        if producto in ventas_por_producto:
                            ventas_por_producto[producto].append(valor)
                        else:
                            ventas_por_producto[producto] = [valor]
                    except ValueError:
                        print(f"Formato incorrecto en venta: {venta}")
    except FileNotFoundError:
        print(f"Error: el archivo '{filename}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

    return ventas_por_producto


def imprimir_totales_y_promedios(ventas_por_producto):
    for producto, montos in ventas_por_producto.items():
        total = sum(montos)
        promedio = total / len(montos)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
