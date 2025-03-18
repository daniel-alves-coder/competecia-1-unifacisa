menu = ["Adicionar","Remover","Ver lista","sair"]
numeros = 1
opcao = 0
filmes = [ ]
def verFilmes(numeros):
    print("ESTES SÃO OS FILMES ATUAIS")
    for ite in filmes:
        print(numeros,"-", ite)
        numeros = numeros + 1
    numeros

while opcao != 4:
    print("MENU - LOCADORA\n------------------")
    for item in menu:
        print(numeros, "-", item)
        numeros = numeros + 1
    numeros = 1
    
    print("------------------")
    opcao = int(input("Digite a Opção: "))
    print("------------------")

    if opcao == 1:
        novoFilme = input("Digite o novo titulo: ")
        filmes.append(novoFilme)
    elif opcao == 2:
        filmeRemover = int(input("Digite o código do título: "))
        if 1 <= filmeRemover <= len(filmes):  # Verifica se está dentro do intervalo válido
            filmes.pop(filmeRemover - 1)
        else:
            print("Código inválido!")
    elif opcao == 3:
        verFilmes(numeros)
    elif opcao != 4:
        print("Opção invalida")

