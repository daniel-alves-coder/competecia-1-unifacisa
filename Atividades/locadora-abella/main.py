opcao = 1

filmes = []
while opcao != 6:
    print("\n1) Listar \n2) Adicionar \n3) Pesquisar \n4) Remover \n5) Substituir \n6) Sair")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        if len(filmes) == 0:
            print("Não existem filmes a serem exibidos")
        else:
            print("Lista de Itens")
            for item in filmes:
                print("-", item)

    elif opcao == 2:
        novoFilme = input("Digite o nome do novo filme: ")

        if len(novoFilme) == 0:
            print("Nome do filme inválido!")
        else:
            filmes.append(novoFilme)
            print("Filme adicionado com sucesso!")

    elif opcao == 3:
        codigoFilme = int(input("Digite o código do filme: "))

        if codigoFilme >= 1 and codigoFilme <= len(filmes):
            filmePesquisado = filmes[codigoFilme - 1]
            print("O filme pesquisado foi", filmePesquisado)
        else:
            print("Código inválido!")

    elif opcao == 4:
        codigoFilme = int(input("Digite o código do filme a remover: "))

        if codigoFilme >= 1 and codigoFilme <= len(filmes):
            filmes.pop(codigoFilme - 1)
            print("Filme removido com sucesso!")

        else:
            print("Código informado inválido!")


    elif opcao == 5:
        codigoFilme = int(input("Digite o código do filme a substituir: "))

        if codigoFilme >= 1 and codigoFilme <= len(filmes):
            nomeNovoFilme = input("Digite o nome do novo filme: ")
            filmes[codigoFilme - 1] = nomeNovoFilme
            print("Filme substituído com sucesso!")

        else:
            print("Código inválido!")

    elif opcao != 6:
        print("Opção Inválida!")

print("Obrigado por usar a Locadora de Italo!")