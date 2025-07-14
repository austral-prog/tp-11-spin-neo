def read_file_to_dict(nombre_archivo):
    ventas = {}
    try:
        with open(nombre_archivo, 'r') as archivo:
            linea = archivo.readline().strip()
            items = linea.split(';')
            for item in items:
                if item:  # Evita procesar cadenas vacías
                    try:
                        producto, valor = item.split(':')
                        valor = float(valor)
                        if producto in ventas:
                            ventas[producto].append(valor)
                        else:
                            ventas[producto] = [valor]
                    except ValueError:
                        print(f" Error de formato en: '{item}'")
        return ventas
    except FileNotFoundError:
        print(f" Error: el archivo '{nombre_archivo}' no existe.")
        return {}
    
def process_dict(ventas):
    for producto, montos in ventas.items():
        if montos:
            total = sum(montos)
            promedio = total / len(montos)
            print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
        else:
            print(f"{producto}: sin ventas registradas.")