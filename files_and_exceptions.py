def read_file_to_dict(filename):
    sales_dict = {}
    try:
        with open(filename, 'r') as file:
            line = file.readline().strip()
            sales = line.split(';')
            for item in sales:
                if item:
                    product, value = item.split(':')
                    value = float(value)
                    if product not in sales_dict:
                        sales_dict[product] = []
                    sales_dict[product].append(value)
    except FileNotFoundError:
        print(f"Error: el archivo '{filename}' no existe.")
    except ValueError:
        print("Error: formato incorrecto en los valores de venta.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    
    return sales_dict

def process_dict(sales_dict):
    for product, values in sales_dict.items():
        total = sum(values)
        average = total / len(values)
        print(f"{product}: ventas totales ${total:.2f}, promedio ${average:.2f}")
