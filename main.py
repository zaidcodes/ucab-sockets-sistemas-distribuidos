import sys
import menu as menu
import client as socketClient

import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

op = -1
client = socketClient.Client("10.2.126.2", 19876 )

while op != 0:
    clear()
    menu.mainMenu(client.nombre)
    op = input("Opción: ")
    if op == "1":
        if not client.isLogged():
            usuario = input("Usuario: ")
            client.login(usuario)
        else:
            client.logout()
    elif op == "2":
        print("nei")
    elif op == "3":
        print("nei")
    elif op == "4":
        print("nei")
    elif op == "5":
        print("nei")
    elif op == "0":
        break