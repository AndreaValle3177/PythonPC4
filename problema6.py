import os

def contar_lineas_codigo(ruta_archivo):
    if not ruta_archivo.endswith('.py'):
        print("El archivo debe tener una extensión .py.")
        return

    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            conteo_lineas = 0

            for linea in lineas:
                linea = linea.strip()
                if linea and not linea.startswith('#'):
                    conteo_lineas += 1
            
            print(f"Número de líneas de código en '{ruta_archivo}': {conteo_lineas}")
    
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    contar_lineas_codigo(ruta_archivo)

if __name__ == "__main__":
    main()
