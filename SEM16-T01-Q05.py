def matricula():
    discio = {}

    while True:
        # Verificar condição
        matricula = input().strip()
        if (matricula == ''):
            break

        # Entradas
        nome = input().strip()
        nota_1 = float(input().strip())
        nota_2 = float(input().strip())
        # Media
        media = calcula_media(nota_1, nota_2)

        # ìndice Matricula
        discio[matricula] = {}
        # Nome aulo
        discio[matricula]['Nome'] = nome
        # Média
        discio[matricula]['Média'] = round(media, 1)

    return discio


def calcula_media(n1, n2):
    return (n1 + n2) / 2


def consulta_matricula(dic):
    lista = []

    while True:
        # Verificar condição
        matricula = input().strip()
        if (matricula == ''):
            break
        lista.append(matricula)

    for matricula in lista:
        print(f"{dic[matricula]['Nome']}: {dic[matricula]['Média']}")


def main():
    dic = matricula()
    consulta_matricula(dic)
    # imprimir(dic)
    # print(dic)


if __name__ == '__main__':
    main()