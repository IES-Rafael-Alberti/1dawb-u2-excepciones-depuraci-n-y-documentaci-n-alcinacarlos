def comprobar_entero(input_de_usuario: str) -> int:
    """Comprobar si es entero

    Args:
        input_de_usuario (str): input de usuario.
    
    Returns:
        int: número introducido por el usuario.
    """
    numero = None
    try:
        numero = int(input_de_usuario)
    except ValueError as e:
        print("**Error** La entrada no es correcta: " , e)
    return numero

def main():
    numero = comprobar_entero(input("Introduce un número: "))
    if numero != None:
        print(numero)


if __name__ == "__main__":
    main()