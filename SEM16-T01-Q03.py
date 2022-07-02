"""Crie um programa que cadastre informações de 20 pessoas (nome, idade e cpf) e coloque em
um dicionário. Após a leitura, remova todas as pessoas menores de 18 anos do dicionário e
coloque-as separadas em outro dicionário. Imprima os dois dicionários separando os campos
por ; (ponto-e-vírgula)."""

"""02.Crie um programa que, usando dicionário, crie uma agenda de tamanho fornecido 
inicialmente pelo usuário. Leia os dados de todos os contatos do usuário (nome, cidade, 
estado, telefone) de forma que a agenda fique completa e por fim imprima todos os contatos. 
Crie um código numérico sequencial para usar como chave do dicionário."""


def cadastrando():
    discio = {}

    for vezes in range(20):
        # Entradas
        nome = input().strip()
        idade = int(input().strip())
        cpf = input().strip()

        discio[cpf] = (nome, idade, cpf)

    return discio


def imprimir(dic):
    de_maior = []
    de_menor = []
    for chave in dic:
        nome, idade, cpf = dic[chave]

        if idade >= 18:
            de_maior.append(dic[chave])
        else:
            de_menor.append(dic[chave])

    print("========== MAIORES DE 18 ANOS ==========")
    for dados in de_maior:
        nome, idade, cpf = dados
        print(f"{nome};{idade};{cpf}")
    print("========== MENORES DE 18 ANOS ==========")
    for dados in de_menor:
        nome, idade, cpf = dados
        print(f"{nome};{idade};{cpf}")


def main():
    dic = cadastrando()
    imprimir(dic)


if __name__ == '__main__':
    main()