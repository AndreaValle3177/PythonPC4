import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    fuentes_disponibles = figlet.getFonts()

    fuente_usuario = input("Ingrese el nombre de la fuente (o presione Enter para una fuente aleatoria): ")

    if not fuente_usuario:
        fuente_seleccionada = random.choice(fuentes_disponibles)
        print(f"Fuente aleatoria seleccionada: {fuente_seleccionada}")
    else:
        if fuente_usuario in fuentes_disponibles:
            fuente_seleccionada = fuente_usuario
        else:
            print(f"Fuente '{fuente_usuario}' no válida. Se seleccionará una fuente aleatoria.")
            fuente_seleccionada = random.choice(fuentes_disponibles)
            print(f"Fuente aleatoria seleccionada: {fuente_seleccionada}")

    figlet.setFont(font=fuente_seleccionada)

    texto = input("Ingrese el texto a imprimir: ")

    print(figlet.renderText(texto))

if __name__ == "__main__":
    main()




