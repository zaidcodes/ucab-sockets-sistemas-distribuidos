import socket
import sys

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, direccionIp, puerto):
        self.nombre = ""
        self.logged = False
        self.server = (direccionIp, puerto)
    
    def login(self, nombre = ""):
        self.sock.connect(self.server)
        resultado = ""
        try:
            mensaje = "helloiam " + nombre
            mensaje_encoded = mensaje.encode("utf8")
            self.sock.sendall(mensaje_encoded)

            while resultado != "ok":
                data = self.sock.recv(2)
                resultado = data.decode("utf8")
        finally:
            if resultado == "ok":
                self.logged = True
                self.nombre = nombre

    def logout(self):
        resultado = ""
        try:
            mensaje = "bye"
            mensaje_encoded = mensaje.encode("utf8")
            self.sock.sendall(mensaje_encoded)
            
            while resultado != "ok":
                data = self.sock.recv(2)
                resultado = data.decode("utf8")

        finally:
            if resultado == "ok":
                self.logged = False
                self.nombre = ""
                self.sock.close()
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            else:
                print("No se pudo cerrar la conexion. Resultado: ", resultado)

    def isLogged(self):
        return self.logged
        