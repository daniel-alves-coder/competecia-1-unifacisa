filmes = [ "f1", "f2", "f3" ]

codigoFilme = int(input("Digite o código do filme: "))

if codigoFilme >= 1 and codigoFilme <= len(filmes):
    filmePesquisado = filmes[codigoFilme-1]
    print("O filme pesquisado foi", filmePesquisado)
else:
    print("Código inválido!")


