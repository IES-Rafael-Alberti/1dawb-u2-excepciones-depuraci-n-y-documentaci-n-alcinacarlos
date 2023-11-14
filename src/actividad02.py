if __name__ == "__main__":
    from actividad01 import pedirint

def impares(num:int) -> str:
    """
    Args:
        num (int): numero introducido por el usuario
        
    Returns:
        str: contiene todos los numeros impares desde 1 hasta ese número separados por comas.
    """
    
    resultado = ""
    for n in range(1, num + 1, 2):
        resultado += str(n)+ ", "
    return resultado[:-2]

def main():
    numero = pedirint("Introduce un numero (no puede ser negativa): ")
    if numero != None:
        print(impares(numero))


if __name__ == "__main__":
    main()