def pedirint_bucle(msg: str) -> int:
    """Solicita un número

    Args:
        msj (str): mensaje que se muestra en consola para solicitar el número.
    
    Returns:
        int: número introducido por el usuario.
    """
    numero = None
    numeroint = None
    while numeroint == None:
        try:
            numero = int(input(msg))
            if numero <= 0:
                raise NameError("**Error** No puedes introducir un número negativo")
            numeroint = numero
            return numeroint
        except NameError as e:
            print(e)
        except:
            print("**Error** Edad introducido no válido")

def cuenta_atras(num:int) -> str:
    """
    Args:
        num (int): numero introducido por el usuario
        
    Returns:
        str: contiene la cuenta atrás desde num hasta cero separados por comas.
    """
    resultado = ""
    for n in range(num, -1, -1):
        if n == 0:
            resultado += str(n)
        else:
            resultado += str(n) + ", "
            
    return resultado

def main():
    numero = pedirint_bucle("Introduce un numero (no puede ser negativa): ")
    if numero != None:
        print(cuenta_atras(numero))


if __name__ == "__main__":
    main()