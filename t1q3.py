def calculaMedia():
    somatorio = 0
    for i in range(100):
        somatorio += int(input())
    media = somatorio / 100

    return media


def main():
    media = calculaMedia()
    print(media)

if __name__ == '__main__':
    main()