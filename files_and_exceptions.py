def read_file(nombre_archivo):
    ventas = {}
    try:
        with open(nombre_archivo, 'r') as archivo:
            linea = archivo.readline().strip()
            items = linea.split(';')
            for item in items:
                if item:
                    producto, valor = item.split(':')
                    valor = float(valor)
                    if producto in ventas:
                        ventas[producto].append(valor)
                    else:
                        ventas[producto] = [valor]
        return ventas
    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_archivo}' no existe.")
        return {}
    except ValueError:
        print("Error: formato incorrecto en algún valor de venta.")
        return {}

def process_dict(ventas):
    for producto, montos in ventas.items():
        if montos:
            total = sum(montos)
            promedio = total / len(montos)
            print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
        else:
            print(f"{producto}: sin ventas registradas.")
