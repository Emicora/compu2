import asyncio
import socket
from PIL import Image
import io

async def send_to_scale_server(image_data):
    # Conecta al segundo servidor para el escalado
    reader, writer = await asyncio.open_connection('localhost', 8889)
    
    # Envía la imagen al segundo servidor
    writer.write(image_data)
    await writer.drain()
    
    # Recibe la imagen escalada
    scaled_data = await reader.read(10000)
    
    writer.close()
    await writer.wait_closed()
    
    return scaled_data

async def handle_client(reader, writer):
    # Recibe la imagen y convierte a escala de grises
    data = await reader.read(10000)  # Ajusta el tamaño si es necesario
    image = Image.open(io.BytesIO(data)).convert("L")
    
    # Guarda la imagen en un buffer para enviarla al servidor de escalado
    output = io.BytesIO()
    image.save(output, format='JPEG')
    output.seek(0)
    
    # Envía la imagen al servidor de escalado y recibe la imagen escalada
    scaled_image_data = await send_to_scale_server(output.read())
    
    # Envía la imagen escalada de vuelta al cliente
    writer.write(scaled_image_data)
    await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 8888)
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
