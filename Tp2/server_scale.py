# server_scale.py
import socket
import multiprocessing
import socketserver
from PIL import Image
import io

def scale_image(data, scale_factor):
    # Abrimos la imagen y la escalamos
    image = Image.open(io.BytesIO(data))
    width, height = image.size
    scaled_image = image.resize((int(width * scale_factor), int(height * scale_factor)))
    
    # Guardamos la imagen escalada en un buffer
    output = io.BytesIO()
    scaled_image.save(output, format='JPEG')
    output.seek(0)
    return output.read()

class ScaleRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Recibe la imagen del primer servidor y aplica el escalado
        data = self.request.recv(10000)  # Ajusta el tamaño del buffer si es necesario
        scale_factor = 0.5  # Define el factor de escala
        scaled_image = scale_image(data, scale_factor)
        
        # Envía la imagen escalada de vuelta al primer servidor
        self.request.sendall(scaled_image)

def start_server():
    # Inicia el servidor de escalado en un proceso separado
    with socketserver.TCPServer(('localhost', 8889), ScaleRequestHandler) as server:
        server.serve_forever()

if __name__ == '__main__':
    multiprocessing.Process(target=start_server).start()
