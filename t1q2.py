def eh_par(numero):
    return numero % 2 == 0


def paresEImpares():
    pares = 0
    impares = 0

    for i in range(100):
        entrada = int(input())
        if eh_par(entrada):
            pares +=1
        else:
            impares += 1
        
    return pares, impares

def main():
    pares, impares = paresEImpares()
    print(f'{pares}')
    print(f'{impares}')


if __name__ == '__main__':
    main()