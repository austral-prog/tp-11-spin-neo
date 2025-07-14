def read_file_to_dict(nombre_archivo):
    ventas = {}
    with open(nombre_archivo, 'r') as archivo:
        linea = archivo.readline().strip()
        items = linea.split(';')
        for item in items:
            if item:  # Evita procesar cadenas vacías
                producto, valor = item.split(':')
                valor = float(valor)
                if producto in ventas:
                    ventas[producto].append(valor)
                else:
                    ventas[producto] = [valor]
    return ventas


def process_dict(ventas):
    for producto in sorted(ventas.keys()):
        montos = ventas[producto]
        if montos:
            total = sum(montos)
            promedio = total / len(montos)
            print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
        else:
            print(f"{producto}: sin ventas registradas.")
