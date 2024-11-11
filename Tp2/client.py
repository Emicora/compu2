# client.py
import asyncio

async def send_image(image_path):
    reader, writer = await asyncio.open_connection('localhost', 8888)
    
    with open(image_path, 'rb') as f:
        writer.write(f.read())
    
    await writer.drain()
    processed_data = await reader.read(10000)  # Ajusta el tamaño según sea necesario
    
    with open('imagen2.jpg', 'wb') as f:
        f.write(processed_data)
    
    writer.close()
    await writer.wait_closed()

asyncio.run(send_image('/home/emicoratolo/Escritorio/tp2Computacion/imagen.jpg'))
