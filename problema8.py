import csv
import sqlite3

sqlite_con = sqlite3.connect('base.db')
cursor = sqlite_con.cursor()

def obtener_tipo_cambio_soles(fecha):
    cursor.execute('SELECT compra, venta FROM sunat_info WHERE fecha = ?', (fecha,))
    tipo_cambio = cursor.fetchone()
    if tipo_cambio:
        return tipo_cambio[1]  
    else:
        return None  

with open('ventas.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    print(f"{'Producto':<20}{'Precio Dólares':<20}{'Fecha Compra':<20}{'Precio Soles':<20}")
    print("="*80)
    
    for row in csv_reader:
        producto = row['producto']
        precio_dolares = float(row['precio_dolares'])
        fecha_compra = row['fecha_compra']
        
        tipo_cambio_soles = obtener_tipo_cambio_soles(fecha_compra)
        
        if tipo_cambio_soles:
    
            precio_soles = precio_dolares * tipo_cambio_soles
        
            print(f"{producto:<20}{precio_dolares:<20}{fecha_compra:<20}{precio_soles:<20.2f}")
        else:
            print(f"No se encontró tipo de cambio para la fecha {fecha_compra}")

sqlite_con.close()
