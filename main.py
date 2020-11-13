import sys
from client import *

import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

try:
    ip_server = sys.argv[1]
    port_server = sys.argv[2]
    username = sys.argv[3]

    client = Client(ip_server, port_server)
    client.hello(username)
    client.msglen()
    client.givememsg()
    client.chkmsg()
    client.bye()
    # clear()
    print("*"*7, "Su mensaje es", "*"*7, "\n\n")
    print(" "*4, client.message)
    print("\n\n")
except Exception as e:
    print("Vuelva a internarlo nuevamente. [", e,"]")
finally:
    print("\nHasta luego\n")