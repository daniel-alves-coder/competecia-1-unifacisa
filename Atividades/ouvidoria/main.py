manifestacoes = [ ]
opcao = 0
barra = "-" * 50
posMenu = False

while opcao != 5:
    print(barra)
    print("1) Listagem das Manifestações")
    print("2) Criar uma nova Manifestação")
    print("3) Exibir quantidade de manifestações")
    print("4) Pesquisar uma manifestação por código")
    print("5) Sair do Sistema")
    print(barra)

    if posMenu:
        print("Sua resposta esta acima do menu")
        print(barra)

    opcao = int(input("Digite o codigo da opção: "))
    print(barra)

    if opcao == 1: #Listagem das Manifestações
        if len(manifestacoes) == 0:
            print("Nenhuma manifestação até o momento!")
        else:
            print("MANIFESTAÇÕES:")
            for index in range(len(manifestacoes)):
                print("manifestação " + str(index + 1) + ") " + manifestacoes[index])

    elif opcao == 2: #Criar uma nova Manifestação
        novaManifestacao = input("Digite a sua manifestação: ")
        manifestacoes.append(novaManifestacao)
        print("Manifestação cadastrada com sucesso o seu codigo é " + str(len(manifestacoes)))

    elif opcao == 3: #Exibir quantidade de manifestações
        if len(manifestacoes) == 0:
            print("Nenhuma manifestação até o momento!")
        elif len(manifestacoes) == 1:
            print("Até o momento, o sistema possui somente 1 manifestação")
        else:
            print("Até o momento, o sistema possui exatas " + str(len(manifestacoes)) + " manifestações")

    elif opcao == 4: #Pesquisar uma manifestação por código
        codigo = int(input("Digite o codigo da manifetação: "))

        if codigo < 1 or codigo > len(manifestacoes): #verifica se o codigo é valido
            print("CODIGO DE MANIFESTAÇÃO INVALIDO")
        else:
            print(barra)
            print("Manifestação de codigo " + str(codigo) + ": ")
            print(manifestacoes[codigo - 1])

    elif opcao != 5: #Caso o usuario digite uma opção que não existe
        print("OPÇÃO INVALIDA")

    posMenu = True

print("OBRIGADO POR USAR NOSSO SISTEMA!")