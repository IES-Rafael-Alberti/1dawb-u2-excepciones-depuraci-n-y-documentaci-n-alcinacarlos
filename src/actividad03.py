from actividad01 import pedirint

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
    numero = pedirint("Introduce un numero (no puede ser negativa): ")
    if numero != None:
        print(cuenta_atras(numero))


if __name__ == "__main__":
    main()