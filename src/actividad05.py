def comprobar_contraseña(password_usuario: str) -> bool:
    """Solicita un número

    Args:
        password_usuario (str): contraseña introducida por el usuario.
    
    Returns:
        bool: True si la contraseña es válida y False si la contraseña es inválida.
    """
    contraseña = "password"
    try:
        if contraseña == password_usuario:
            return True
        else:
            raise NameError("Incorrect Password!!")
    except NameError as e:
        print(e)
        return False

def main():
    password = input("Introduce la contraseña: ")
    if comprobar_contraseña(password) == True:
        print("Contraseña correcta.")


if __name__ == "__main__":
    main()