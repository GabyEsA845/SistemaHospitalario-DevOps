usuarios_registrados = {"admin": "1234"}

def login(usuario, contraseña):
    if usuario in usuarios_registrados and usuarios_registrados[usuario] == contraseña:
        return True
    return False