import sys
import socket
import base64
import hashlib
from exceptions import *

class Client:

    def __init__(self, ip = "127.0.0.1", port = 19876):
        self.ip = str(ip)
        self.tcp_port = int(port)
        self.udp_port = 19879
        self.sock_tcp = None
        self.sock_udp = None
        self.message_len = None
        self.message = None
        self.b64_message = None
        self.md5_message = None
        tcp_sock = self.get_sock_tcp()
        local_ip = tcp_sock.getsockname()[0]
        self.get_sock_udp()

    def send_message(self, message = ""):
        response = ""
        sock = self.get_sock_tcp()
        try:
            message_encoded = message.encode("utf-8")
            sock.sendall(message_encoded)

            while len(response) < 2:
                response = sock.recv(1024)
        finally:
            if len(response) > 2:
               response = response.decode("utf-8")
        return response

    def listen_message(self):
        response = ""
        sock = self.get_sock_udp()
        try:
            while len(response) < self.message_len:
                response = sock.recv(2048)
        finally:
            if len(response) > 0:
               response = response.decode("utf-8")
        return response

    def get_sock_tcp(self):
        if self.sock_tcp is None:
            self.sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock_tcp.settimeout(20.0)
            self.sock_tcp.connect((self.ip, self.tcp_port))
        return self.sock_tcp
    
    def get_sock_udp(self):
        local_ip = self.local_ip()
        if self.sock_udp is None:
            self.sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock_udp.settimeout(20.0)
            self.sock_udp.bind((local_ip, self.udp_port))
        return self.sock_udp
    
    def local_ip(self):
        sock = self.get_sock_tcp()
        client_ip = sock.getsockname()[0]
        return client_ip

    def hello(self, username = "usuario_1"):
        client_ip = self.local_ip()
        message = "helloiam " + username
        response = self.send_message(message)

        if response.find("invalid user name") != -1:
            raise InvalidUserNameException(username)
        elif response.find("invalid src ip") != -1:
            raise InvalidSrcIpException(client_ip, username)

        return response

    def msglen(self):
        message = "msglen"
        response = self.send_message(message)

        if response.find("error") != -1:
            raise MsgLenErrorException()
        
        self.message_len = int(response.split(" ")[1])

        return self.message_len
    
    def request_message(self):
        message = "givememsg " + str(self.udp_port)
        response = self.send_message(message)

        if response.find("invalid udp port") != -1:
            raise InvalidUdpPortException(self.udp_port)

        return response
    
    def givememsg(self):
        valid_len = False
        max_attempts = 3
        attempt = 0

        while valid_len == False and attempt < max_attempts:
            self.request_message()
            print("Intentando recuperar el mensaje intento [", attempt + 1, "]")
            try:
                self.b64_message = self.listen_message()
            except socket.timeout:
                attempt = attempt + 1

            try:
                if self.b64_message:
                    message = self.decode_base64()
                    self.encode_md5()
                    if len(message) == self.message_len:
                        valid_len = True
            except Exception as e:
                print("error:::", e)
                print("Valid len",valid_len)
        if attempt == max_attempts and not valid_len:
            raise MaxAttemptsUdpMessageException(max_attempts)
        return message

    def decode_base64(self):
        message = self.b64_message.encode("utf-8")
        self.message = base64.decodebytes(message).decode("utf-8")
        return self.message
    
    def encode_md5(self):
        self.md5_message = hashlib.md5(self.message.encode('utf-8')).hexdigest()
        return self.md5_message
    
    def chkmsg(self):
        message = "chkmsg " + self.md5_message
        response = self.send_message(message)

        if response.find("invalid checksum format") != -1:
            raise InvalidChecksumFormatException(self.md5_message)
        elif response.find("bad checksum") != -1:
            raise BadChecksumException(self.md5_message)

        return response

    def bye(self):
        sock = self.get_sock_tcp()
        message = "bye"
        response = self.send_message(message)
        sock.close()
        return response
