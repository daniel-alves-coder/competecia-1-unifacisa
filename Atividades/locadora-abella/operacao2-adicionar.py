filmes = [ ]

novoFilme = input("Digite o nome do novo filme: ")

if len(novoFilme) == 0:
    print("Nome do filme inválido!")
else:
    filmes.append(novoFilme)
    print("Filme adicionado com sucesso!")

print(len(filmes))