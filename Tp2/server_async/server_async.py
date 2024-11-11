# server_async/server_async.py
import asyncio
from PIL import Image
import io

async def send_to_scale_server(image_data):
    reader, writer = await asyncio.open_connection('localhost', 8889)
    writer.write(image_data)
    await writer.drain()
    
    scaled_image_data = await reader.read(10000)
    writer.close()
    await writer.wait_closed()
    return scaled_image_data

async def handle_client(reader, writer):
    data = await reader.read(10000)
    image = Image.open(io.BytesIO(data)).convert("L")
    
    output = io.BytesIO()
    image.save(output, format='JPEG')
    output.seek(0)
    
    scaled_image_data = await send_to_scale_server(output.read())
    
    writer.write(scaled_image_data)
    await writer.drain()
    writer.close()

async def start_async_server(ip, port):
    server = await asyncio.start_server(handle_client, ip, port)
    print(f'Servidor asincrónico iniciado en {ip}:{port}')
    async with server:
        await server.serve_forever()
