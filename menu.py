def mainMenu(name = ""):
    saludo = "" if (name == "") else "- " + name
    print("*"*6, " Cliente Socket", saludo, "*"*6, end="\n\n")
    print("::"*7, "Menú principal" ,"::"*7)
    print("1.","Iniciar conexión" if (name == "") else "Cerrar conexión")
    print("2. Obtener longitud del mensaje")
    print("3. Obtener mensaje")
    print("4. Validar mensaje")
    print("5. Realizar todo")
    print("0. Salir")