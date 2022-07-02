
def qtd_vogais():

    discio = {'A' :0, 'E' :0, 'I' :0, 'O' :0, 'U' :0}

    texto = input().strip()
    for letra in texto.lower():

        if letra == 'a' or letra == 'á' or letra == 'â' or letra == 'ã':
            na = discio['A']
            na +=1
            discio['A'] = na

        if letra == 'e' or letra == 'é' or letra == 'ê':
            ne = discio['E']
            ne +=1
            discio['E'] = ne

        if letra == 'i' or letra == 'í' or letra == 'î':
            ni = discio['I']
            ni +=1
            discio['I'] = ni

        if letra == 'o' or letra == 'ó' or letra == 'ô 'or letra == 'õ':
            no = discio['O']
            no += 1
            discio['O'] = no

        if letra == 'u' or letra == 'ú' or letra == 'û':
            nu = discio['U']
            nu +=1
            discio['U'] = nu

    return discio


def imprimir(dic):

    print('A:' ,dic['A'])
    print('E:' ,dic['E'])
    print('I:' ,dic['I'])
    print('O:' ,dic['O'])
    print('U:' ,dic['U'])



def main():
    texto = qtd_vogais()
    imprimir(texto)


if __name__ == '__main__':
    main()