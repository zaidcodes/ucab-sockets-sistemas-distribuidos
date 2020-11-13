class InvalidUserNameException(Exception):
    message = 'El usuario {usuario} no registrado en el servidor'

    def __init__(self, usuario):
        self.usuario = usuario
        super().__init__(self.message.format(usuario = usuario))


class InvalidSrcIpException(Exception):
    message = 'La dirección ip {ip} del cliente no coincide con el registro del usuario {usuario}'

    def __init__(self, ip, usuario):
        self.usuario = usuario
        self.ip = ip
        super().__init__(self.message.format(ip = ip,usuario = usuario))


class MsgLenErrorException(Exception):
    message = 'Ha ocurrido un problema al obtener la longitud del mensaje'

    def __init__(self):
        super().__init__(self.message)


class InvalidUdpPortException(Exception):
    message = 'Puerto UDP {port} inválido'

    def __init__(self, port):
        self.port = port
        super().__init__(self.message.format(port = port))


class InvalidChecksumFormatException(Exception):
    message = 'Formato inválido del checksum {checksum}'

    def __init__(self, checksum):
        self.checksum = checksum
        super().__init__(self.message.format(checksum = checksum))


class BadChecksumException(Exception):
    message = 'El checksum {checksum} no coincide con el de el mensaje enviado'

    def __init__(self, checksum):
        self.checksum = checksum
        super().__init__(self.message.format(checksum = checksum))
