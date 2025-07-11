import requests
from bs4 import BeautifulSoup
import time
import datetime

# --- CONFIGURACIÓN ---
# ¡IMPORTANTE! Un 'User-Agent' simula que la petición viene de un navegador real.
# Puedes buscar "my user agent" en Google para obtener el tuyo.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
# Define el precio deseado. El script te avisará si el precio actual es menor o igual.
PRECIO_DESEADO = 500.00 

# --- FUNCIONES ---

def verificar_precio(url):
    """
    Función principal que entra a una URL, extrae el título y el precio del producto,
    y lo compara con el precio deseado.
    """
    try:
        # 1. Realizar la petición a la página
        pagina = requests.get(url, headers=HEADERS)
        # Activar una excepción si algo salió mal con la petición (ej: error 404 o 500)
        pagina.raise_for_status() 

        # 2. Parsear el HTML con BeautifulSoup
        soup = BeautifulSoup(pagina.content, "html.parser")

        # 3. Encontrar el título y el precio
        # ⚠️ ¡ESTA ES LA PARTE QUE DEBES PERSONALIZAR! ⚠️
        # Haz clic derecho en el título/precio en la web -> Inspeccionar, y busca la etiqueta y su clase/id.
        titulo = soup.find("h1", {"class": "ui-pdp-title"}).get_text().strip()
        span_precio = soup.find("span", {"class", "andes-money-amount__fraction"}).get_text()

        # 4. Limpiar y convertir el precio a un número (float)
        # Este proceso puede variar mucho entre sitios web.
        precio_limpio = "".join(filter(str.isdigit, span_precio))
        if len(precio_limpio) > 2:
            precio_actual = float(precio_limpio[:-2] + "." + precio_limpio[-2:])
        else:
            precio_actual = float(precio_limpio)


        # 5. Imprimir resultados y comparar precios
        print(f"✅ Producto: {titulo}")
        print(f"   Precio actual: ${precio_actual:,.2f}")

        if precio_actual <= PRECIO_DESEADO:
            print(f"   🎉 ¡OFERTA ENCONTRADA! El precio está por debajo de ${PRECIO_DESEADO:,.2f}")
        else:
            print(f"   😕 El precio aún no ha bajado.")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión al verificar {url}: {e}")
    except AttributeError:
        # Este error ocurre si `find()` no encuentra la etiqueta y devuelve 'None'.
        print(f"❌ No se pudo encontrar el título o el precio en {url}. Revisa los selectores de CSS.")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado con {url}: {e}")


# --- EJECUCIÓN DEL SCRIPT ---
if __name__ == "__main__":
    print("-" * 50)
    print(f"Iniciando Vigilante de Ofertas - {datetime.date.today()}")
    print("-" * 50)

    try:
        with open("productos.txt", "r") as f:
            urls = [line.strip() for line in f if line.strip()]

        if not urls:
            print("El archivo 'productos.txt' está vacío. Añade algunas URLs.")
        else:
            for url in urls:
                verificar_precio(url)
                print("-" * 25)
                # Pausa para no saturar el servidor con peticiones
                time.sleep(2) 

    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo 'productos.txt'. Asegúrate de que exista.")
    except Exception as e:
        print(f"❌ Ocurrió un error general: {e}")