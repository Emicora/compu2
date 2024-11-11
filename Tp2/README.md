# Guía de Uso para el Proyecto de Procesamiento de Imágenes

Este proyecto permite procesar imágenes de manera asíncrona usando dos servidores: el primero convierte la imagen a escala de grises y el segundo reduce su tamaño en un 50%. La arquitectura está diseñada para manejar múltiples conexiones y procesar imágenes en paralelo, utilizando asyncio para la asincronía y multiprocessing para el procesamiento en paralelo.
## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener las siguientes dependencias instaladas:

    Python 3.8 o superior
    Paquete Pillow para el procesamiento de imágenes

Para instalar Pillow, puedes ejecutar:

    pip install Pillow

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

    TP2/
    ├── main.py                # Archivo principal para iniciar los servidores
    ├── client.py              # Cliente para enviar imágenes al servidor asincrónico
    ├── server_async/          # Carpeta del servidor asincrónico
    │   ├── __init__.py        # Inicialización del módulo
    │   └── server_async.py    # Código del servidor asincrónico
    ├── server_scale/          # Carpeta del servidor de escalado
    │   ├── __init__.py        # Inicialización del módulo
    │   └── server_scale.py    # Código del servidor de escalado
    ├── imagen.jpg             # Ejemplo de imagen para procesar
    └── README.md              # Documentación de uso

## Instrucciones de Uso
### Paso 1: Ejecutar el Proyecto desde main.py

Este archivo es el punto de entrada para ejecutar ambos servidores. Al iniciarse, main.py lanza el servidor de escalado en un proceso separado y luego inicia el servidor asincrónico en la IP y el puerto especificados.

Para ejecutarlo, usa el siguiente comando, especificando la dirección IP y el puerto para el servidor asincrónico:

    python3 main.py -i 127.0.0.1 -p 8888

Este comando:

    - Inicia el servidor de escalado en el puerto 8889, que se encargará de reducir el tamaño de las imágenes.
    - Inicia el servidor asincrónico en el puerto 8888, que manejará las conexiones del cliente, convertirá las imágenes a escala de grises y las enviará al servidor de escalado para el procesamiento final.
### Paso 2: Ejecutar el Cliente (client.py)

El cliente se conecta al servidor asincrónico, envía una imagen y espera recibir la imagen procesada. Este paso puede realizarse en una terminal separada mientras los servidores están en ejecución.

Para ejecutarlo, usa el siguiente comando:

    python3 client.py

Este comando enviará la imagen imagen.jpg (o cualquier otra imagen que especifiques) al servidor asincrónico. La imagen procesada (en escala de grises y con tamaño reducido) se guardará localmente como processed_image.jpg en el mismo directorio del proyecto.
### Ejemplo Completo de Flujo
1. Inicia el proyecto desde main.py en una terminal:

    python3 main.py -i 127.0.0.1 -p 8888

2. En otra terminal, ejecuta el cliente para enviar la imagen:

    python3 client.py

Asegúrate de tener el archivo imagen.jpg en el directorio actual o especifica la ruta completa de una imagen existente en el archivo client.py.

## Notas Adicionales

    Configuración de Escalado: En server_scale.py, el factor de escala está configurado en 0.5 (50% de reducción). Puedes ajustar este valor según tus necesidades.
    Puertos: Por defecto, el servidor asincrónico usa el puerto 8888 y el servidor de escalado el 8889. Si necesitas cambiarlos, asegúrate de hacerlo en los archivos correspondientes (main.py y server_scale.py) para que coincidan.

## Ejemplo de Uso en Consola

    Ejecuta main.py para iniciar ambos servidores en diferentes terminales.
    Ejecuta client.py para enviar la imagen y recibirla procesada.