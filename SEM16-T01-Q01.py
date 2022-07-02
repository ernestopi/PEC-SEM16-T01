def discionario():
    discio = {}
    indices = 101

    while True:
        # Verificar condição
        nome_livro = input("Insira o titulo do livro: ").strip() #Titulo do livro
        if (nome_livro == ''):
            break

        # Entradas
        isbn = input("Insira o ISBN: ").strip() #ISBN
        autor = input("Insira o autor do livro: ").strip() #Autor do livro
        preco = float(input("Insira o preço do livro: ").strip()) #preço do livro

        # Código
        discio[indices] = {}
        # titulo
        discio[indices]['Título'] = nome_livro
        # isbn
        discio[indices]['ISBN'] = isbn
        # autor
        discio[indices]['Autor'] = autor
        # preço
        discio[indices]['Preço'] = f"{preco:.2f}"

        # Indice
        indices += 1

    return discio


def main():
    dic = discionario()

    for chave in dic:
        titulo, isbn, autor, preco = dic[chave]

        # Info
        titulo = dic[chave][titulo]
        isbn = dic[chave][isbn]
        autor = dic[chave][autor]
        preco = dic[chave][preco]

        print(f"Código: {chave}")
        print(f"Título: {titulo}")
        print(f"ISBN: {isbn}")
        print(f"Autor: {autor}")
        print(f"Preço: {preco}")


if __name__ == '__main__':
    main()