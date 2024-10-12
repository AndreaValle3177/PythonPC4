import requests
import sqlite3
from pymongo import MongoClient
from datetime import datetime, timedelta

mongo_client = MongoClient('mongodb+srv://andreavalle3100:9fJhN6AP3PrZ3RLc@mongoldb.e89mt.mongodb.net/?retryWrites=true&w=majority&appName=MongolDB')
mongo_db = mongo_client['sunat_db']
mongo_collection = mongo_db['sunat_info']

def obtener_precio_dolar():
    url = "https://apis.net.pe/v1/tipo-cambio"
    precios_dolar = []

    
    fecha_inicio = datetime(2023, 1, 1)
    fecha_fin = datetime(2023, 12, 31)
    

    while fecha_inicio <= fecha_fin:
        response = requests.get(f"{url}?fecha={fecha_inicio.strftime('%Y-%m-%d')}")
        if response.status_code == 200:
            data = response.json()
            if data.get('compra') and data.get('venta'):
                precio = {
                    'fecha': fecha_inicio.strftime('%Y-%m-%d'),
                    'compra': data['compra'],
                    'venta': data['venta']
                }
                precios_dolar.append(precio)
        else:
            print(f"Error al obtener datos para {fecha_inicio.strftime('%Y-%m-%d')}")

        fecha_inicio += timedelta(days=1)

    return precios_dolar

def guardar_en_sqlite(precios_dolar):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha TEXT PRIMARY KEY,
            compra REAL,
            venta REAL
        )
    ''')

    for precio in precios_dolar:
        cursor.execute('''
            INSERT OR REPLACE INTO sunat_info (fecha, compra, venta)
            VALUES (?, ?, ?)
        ''', (precio['fecha'], precio['compra'], precio['venta']))

    conn.commit()
    conn.close()

def guardar_en_mongodb(precios_dolar):
    mongo_collection.insert_many(precios_dolar)

def mostrar_contenido_sqlite():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sunat_info")
    rows = cursor.fetchall()
    
    print("Contenido de la tabla sunat_info:")
    for row in rows:
        print(f"Fecha: {row[0]}, Compra: {row[1]}, Venta: {row[2]}")
    
    conn.close()

def main():
    precios_dolar = obtener_precio_dolar()
    if precios_dolar:
        guardar_en_sqlite(precios_dolar)
        guardar_en_mongodb(precios_dolar)
        mostrar_contenido_sqlite()
    else:
        print("No se obtuvieron precios del dólar.")

if __name__ == "__main__":
    main()
