# server_scale/server_scale.py
import socketserver
from multiprocessing import Process
from PIL import Image
import io

def scale_image(data, scale_factor=0.5):
    image = Image.open(io.BytesIO(data))
    width, height = image.size
    scaled_image = image.resize((int(width * scale_factor), int(height * scale_factor)))
    output = io.BytesIO()
    scaled_image.save(output, format='JPEG')
    output.seek(0)
    return output.read()

class ScaleRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(10000)
        scaled_image_data = scale_image(data)
        self.request.sendall(scaled_image_data)

def start_scale_server():
    process = Process(target=_run_scale_server)
    process.start()

def _run_scale_server():
    with socketserver.TCPServer(('localhost', 8889), ScaleRequestHandler) as server:
        print("Servidor de escalado iniciado en localhost:8889")
        server.serve_forever()
