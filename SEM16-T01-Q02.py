def dic_agenda():
    discio = {}
    qtd_ind = int(input())

    for indices in range(qtd_ind):
        # Entradas
        nome = input().strip()
        cidade = input().strip()
        estado = input().strip()
        telefone = input().strip()

        discio[indices] = (nome, cidade + f'({estado})', telefone)

    return discio


def imprimir(dic):
    for chave in dic:
        nome, localidade, telefone = dic[chave]

        # Info

        print(f"{nome:25}{localidade:30}{telefone}")


def main():
    dic = dic_agenda()
    imprimir(dic)


if __name__ == '__main__':
    main()