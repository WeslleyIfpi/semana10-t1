def maiorEntre100():
    maior = -1
    for i in range(100):
        numero = int(input())
        if numero > maior:
            maior = numero

    return maior



def main():
    print(maiorEntre100())


if __name__ == '__main__':
    main()