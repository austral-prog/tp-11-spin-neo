def read_file(producto):
    
    dicc0 = dict()
    
    ventas = {}
    try:
        with open(producto, 'r') as archivo:
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
        print(f"Error: el archivo '{producto}' no existe.")
        return {}
    
def process_dict(ventas):
    for producto, montos in ventas.items():
        total = sum(montos)
        promedio = total / len(montos)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
