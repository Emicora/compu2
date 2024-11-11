# client.py
import asyncio

async def send_image(image_path):
    reader, writer = await asyncio.open_connection('localhost', 8888)
    
    with open(image_path, 'rb') as f:
        writer.write(f.read())
    
    await writer.drain()
    processed_data = await reader.read(10000)
    
    with open('processed_image.jpg', 'wb') as f:
        f.write(processed_data)
    
    writer.close()
    await writer.wait_closed()

# Ejecuta el cliente con la imagen de ejemplo
asyncio.run(send_image('imagen.jpg'))
