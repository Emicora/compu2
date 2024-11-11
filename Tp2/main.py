# main.py
import argparse
import asyncio
from server_async.server_async import start_async_server
from server_scale.server_scale import start_scale_server

def main():
    # Configuración de argparse para capturar IP y puerto desde la línea de comandos
    parser = argparse.ArgumentParser(description="TP2 - procesa imágenes")
    parser.add_argument("-i", "--ip", required=True, help="Dirección de escucha del servidor asincrónico")
    parser.add_argument("-p", "--port", required=True, type=int, help="Puerto de escucha del servidor asincrónico")
    args = parser.parse_args()
    
    # Inicia el servidor de escalado en un proceso separado
    start_scale_server()

    # Inicia el servidor asincrónico con los argumentos de IP y puerto
    asyncio.run(start_async_server(args.ip, args.port))

if __name__ == "__main__":
    main()
