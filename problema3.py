import requests
import zipfile
import os

def descargar_imagen(url, nombre_archivo):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        
        with open(nombre_archivo, 'wb') as file:
            file.write(response.content)
        print(f"Imagen descargada correctamente como {nombre_archivo}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen: {e}")

def crear_zip(nombre_imagen, nombre_zip):
    try:
    
        with zipfile.ZipFile(nombre_zip, 'w') as zipf:
            zipf.write(nombre_imagen, os.path.basename(nombre_imagen))
        print(f"Archivo zip creado correctamente como {nombre_zip}")
    
    except Exception as e:
        print(f"Error al crear el archivo zip: {e}")

def descomprimir_zip(nombre_zip, ruta_extraccion):
    try:
        
        with zipfile.ZipFile(nombre_zip, 'r') as zipf:
            zipf.extractall(ruta_extraccion)
        print(f"Archivo zip descomprimido en {ruta_extraccion}")
    
    except Exception as e:
        print(f"Error al descomprimir el archivo zip: {e}")

def main():

    url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    
    nombre_imagen = "imagen_descargada.jpg"
    nombre_zip = "imagen_comprimida.zip"
    ruta_extraccion = "./"


    descargar_imagen(url_imagen, nombre_imagen)

    crear_zip(nombre_imagen, nombre_zip)

    descomprimir_zip(nombre_zip, ruta_extraccion)

if __name__ == "__main__":
    main()

