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
├── server_async.py          # Primer servidor: procesa la imagen a escala de grises.
├── server_scale.py          # Segundo servidor: escala la imagen.
├── client.py                # Cliente que envía imágenes para ser procesadas.
└── README.md                # Documentación de uso.

## Instrucciones de Uso
### Paso 1: Ejecutar el Servidor de Escalado (server_scale.py)

Este servidor debe estar en ejecución antes de iniciar el servidor principal, ya que es el encargado de reducir el tamaño de la imagen.

Para ejecutarlo, usa el siguiente comando:

python server_scale.py

Este servidor se ejecutará en el puerto 8889 y estará escuchando solicitudes de escalado de imágenes.
### Paso 2: Ejecutar el Servidor Asíncrono (server_async.py)

El servidor principal maneja las conexiones del cliente, convierte la imagen a escala de grises y la envía al servidor de escalado. Una vez recibida la imagen escalada, la envía de vuelta al cliente.

Para ejecutarlo, usa el siguiente comando:

python server_async.py

Este servidor se ejecutará en el puerto 8888 y estará listo para recibir imágenes del cliente.
### Paso 3: Ejecutar el Cliente (client.py)

El cliente se conecta al servidor principal, envía una imagen y espera recibir la imagen procesada.

Ejecuta el cliente con el siguiente comando, reemplazando image_path.jpg con la ruta de la imagen que deseas procesar:

python client.py

La imagen procesada (en escala de grises y con tamaño reducido) se guardará localmente como processed_image.jpg en el mismo directorio del proyecto.
### Ejemplo Completo de Flujo

#### 1.Inicia el servidor de escalado en una terminal:

python server_scale.py

#### 2.Inicia el servidor principal en otra terminal:

python server_async.py

#### 3.Envía una imagen desde el cliente:

    python client.py

    Asegúrate de tener el archivo image_path.jpg en el directorio actual o especifica la ruta completa de una imagen existente.

## Notas Adicionales

    Configuración de Escalado: En server_scale.py, el factor de escala está configurado en 0.5 (50% de reducción). Puedes ajustar este valor según tus necesidades.
    Puertos: Por defecto, el servidor principal usa el puerto 8888 y el servidor de escalado el 8889. Si necesitas cambiarlos, asegúrate de hacerlo en ambos archivos (server_async.py y server_scale.py) para que coincidan.

## Ejemplo de Uso en Consola

    Inicia server_scale.py y server_async.py en diferentes terminales.
    Ejecuta client.py para enviar la imagen y recibirla procesada.