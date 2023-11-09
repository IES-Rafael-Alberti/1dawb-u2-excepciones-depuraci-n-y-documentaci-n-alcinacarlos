def algoritmo_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for x in range(0, n-i-1):
            if lista[x] > lista[x+1]:
                lista[x], lista[x+1] = lista[x+1], lista[x]
    return lista

def main():
    a = [8, 3, 1, 19, 14]
    print(algoritmo_burbuja(a))


if __name__ == "__main__":
    main()
