filmes = [ "f1", "f2", "f3" ]

codigoFilme = int(input("Digite o código do filme a remover: "))

if codigoFilme >= 1 and codigoFilme <= len(filmes):
    filmes.pop(codigoFilme-1)
    print("Filme removido com sucesso!")

else:
    print("Código informado inválido!")
