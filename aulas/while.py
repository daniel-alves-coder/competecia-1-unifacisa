#outra maneira de escrever o comando while

while True:
    op = int(input("informa a opção: "))
    if  op == 4:
        break #significa quebrar
        #quando entrar no break, vai automaticamente sair do while

opcao = 1

while opcao != 4:
    print("Locadora de Leonardo\n1) Listar \n2) Adicionar \n3) Pesquisar \n4) Sair")
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        print("Listar")

    elif opcao == 2:
        print("Adicionar")

    elif opcao == 3:
        print("Pesquisar")

    elif opcao != 4: #essa maneira fica mais limpa de entender o codigo
        #tudo que não for 4 vai entrar aqui
        print("Opção inválida")

