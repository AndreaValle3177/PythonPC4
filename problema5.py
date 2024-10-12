import os

class TablaMultiplicar:
    def generar_tabla(self, n):
        nombre_archivo = f"tabla-{n}.txt"
        try:
            with open(nombre_archivo, 'w') as archivo:
                for i in range(1, 11):
                    archivo.write(f"{n} x {i} = {n * i}\n")
            print(f"Tabla de multiplicar del {n} guardada en {nombre_archivo}")
        except Exception as e:
            print(f"Error al crear el archivo: {e}")

    def leer_tabla(self, n):
        nombre_archivo = f"tabla-{n}.txt"
        try:
            with open(nombre_archivo, 'r') as archivo:
                contenido = archivo.read()
                print(f"Contenido del archivo {nombre_archivo}:\n")
                print(contenido)
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe.")
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")

    def leer_linea_tabla(self, n, m):
        nombre_archivo = f"tabla-{n}.txt"
        try:
            with open(nombre_archivo, 'r') as archivo:
                lineas = archivo.readlines()
                if 1 <= m <= 10:
                    print(f"Línea {m} de la tabla del {n}: {lineas[m-1].strip()}")
                else:
                    print("El número m debe estar entre 1 y 10.")
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe.")
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")


def menu():
    tabla = TablaMultiplicar()
    
    while True:
        print("\nMenú de opciones:")
        print("1. Generar y guardar tabla de multiplicar.")
        print("2. Leer y mostrar tabla de multiplicar.")
        print("3. Leer una línea específica de la tabla de multiplicar.")
        print("4. Salir.")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                tabla.generar_tabla(n)
            else:
                print("El número debe estar entre 1 y 10.")
        
        elif opcion == "2":
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                tabla.leer_tabla(n)
            else:
                print("El número debe estar entre 1 y 10.")
        
        elif opcion == "3":
            n = int(input("Ingrese un número entero entre 1 y 10 para la tabla: "))
            m = int(input("Ingrese un número entero entre 1 y 10 para la línea: "))
            if 1 <= n <= 10 and 1 <= m <= 10:
                tabla.leer_linea_tabla(n, m)
            else:
                print("Ambos números deben estar entre 1 y 10.")
        
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
