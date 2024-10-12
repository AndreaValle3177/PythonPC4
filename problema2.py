import random
from pyfiglet import Figlet

def main():
    # Crear una instancia de Figlet
    figlet = Figlet()

    # Obtener la lista de fuentes disponibles
    fuentes_disponibles = figlet.getFonts()

    # Solicitar al usuario la fuente deseada
    fuente_usuario = input("Ingrese el nombre de la fuente (o presione Enter para una fuente aleatoria): ")

    # Seleccionar una fuente al azar si no se ha ingresado ninguna
    if not fuente_usuario:
        fuente_seleccionada = random.choice(fuentes_disponibles)
        print(f"Fuente aleatoria seleccionada: {fuente_seleccionada}")
    else:
        # Verificar si la fuente ingresada por el usuario es válida
        if fuente_usuario in fuentes_disponibles:
            fuente_seleccionada = fuente_usuario
        else:
            print(f"Fuente '{fuente_usuario}' no válida. Se seleccionará una fuente aleatoria.")
            fuente_seleccionada = random.choice(fuentes_disponibles)
            print(f"Fuente aleatoria seleccionada: {fuente_seleccionada}")

    # Configurar la fuente seleccionada en Figlet
    figlet.setFont(font=fuente_seleccionada)

    # Solicitar al usuario el texto que quiere imprimir
    texto = input("Ingrese el texto a imprimir: ")

    # Renderizar el texto en arte ASCII con la fuente seleccionada
    print(figlet.renderText(texto))

if __name__ == "__main__":
    main()




