import requests

def obtener_precio_bitcoin():

    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        datos = response.json()  
        

        precio_usd = datos['bpi']['USD']['rate_float']
        return precio_usd
    
    except requests.RequestException as e:
        print(f"Error al conectarse a la API: {e}")
        return None

def calcular_valor_bitcoins(n, precio_bitcoin):
   
    return n * precio_bitcoin

def main():
    
    try:
        n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    
    precio_bitcoin = obtener_precio_bitcoin()
    
    if precio_bitcoin is None:
        print("No se pudo obtener el precio del Bitcoin.")
        return
    
    valor_total = calcular_valor_bitcoins(n, precio_bitcoin)
    
    print(f"El valor de {n} Bitcoins es: ${valor_total:,.4f} USD")

if __name__ == "__main__":
    main()

