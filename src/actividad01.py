def pedirint(msg: str) -> int:
    """Solicita un número

    Args:
        msj (str): mensaje que se muestra en consola para solicitar el número.
    
    Returns:
        int: número introducido por el usuario.
    """
    numero = None
    try:
        numero = int(input(msg))
        if numero <= 0:
            raise NameError("**Error** No puedes introducir un número negativo")
    except NameError as e:
        print(e)
    except:
        print("**Error** Edad introducido no válido")
    return numero

def años_cumplidos(edad:int) -> str:
    """
    Args:
        edad (int): edad introducida por el usuario
        
    Returns:
        str: contiene todos los años que ha cumplido el usuario
    """
    if edad != None:
        años_cumplidos = ""
        for i in range(1, edad + 1):
            años_cumplidos += str(i) + "\n"
        return años_cumplidos

def main():
    edad = pedirint("Introduce tu edad (no puede ser negativa): ")
    if edad != None:
        print(años_cumplidos(edad))


if __name__ == "__main__":
    main()