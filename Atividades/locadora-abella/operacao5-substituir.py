filmes = [ "f1", "f2", "f3" ]

codigoFilme = int(input("Digite o código do filme a substituir: "))

if codigoFilme >= 1 and codigoFilme <= len(filmes):
    nomeNovoFilme = input("Digite o nome do novo filme: ")
    filmes[codigoFilme-1] = nomeNovoFilme
    print("Filme substituído com sucesso!")

else:
    print("Código inválido!")