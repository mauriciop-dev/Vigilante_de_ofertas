# 🤖 Vigilante de Ofertas Automatizado

Este es un proyecto en Python que vigila el precio de productos en línea y avisa cuando encuentra una oferta.

## 🚀 ¿Cómo funciona?

El script `main.py` lee una lista de URLs desde el archivo `productos.txt`. Luego, utiliza las librerías `requests` y `BeautifulSoup` para hacer web scraping, extrayendo el nombre y el precio de cada producto.

Finalmente, compara el precio actual con un precio objetivo definido en el script para determinar si es una buena oferta.

## 🛠️ Uso

1.  Clona este repositorio.
2.  Instala las dependencias: `pip install -r requirements.txt`
3.  Añade las URLs de los productos que quieres seguir en `productos.txt`.
4.  ¡Personaliza los selectores CSS en `main.py` para que coincidan con tus sitios web!
5.  Ejecuta el script: `python main.py`

## ⚙️ Automatización

Este proyecto está diseñado para ser automatizado con **GitHub Actions**. El workflow correspondiente se encargará de ejecutar el script periódicamente para buscar ofertas sin intervención manual.