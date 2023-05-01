def imprimeDezEmDez():
    saida = ''
    for i in range(10, 1001, 10):
       saida += str(i) + ', '

    saida = saida.strip(', ')
    saida += '.'

    return saida


def main():
   print( imprimeDezEmDez())

if __name__ == '__main__':
    main()