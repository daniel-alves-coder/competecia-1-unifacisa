#listas são criadas da seguinte maneira
frutas = ["uva", "kiui","maça","pera"]
#=====================================

#ecessão ao fluxo normal = exeption
'''
isso significa que o valor escolhido não exite:

exemplo:
frutas = ["uva", "kiui"]

print(frutas[2])
    isso é um exeption

vai aparecer a seguinte mensagem 
"list index out of range"

'''
#=====================================

#para mostrar por elemento
print(frutas[0])

frutas.append("jaca") #adiciona no final da lista
#append adiciona no final da lista

#maneira mais facil de ler
novaFruta = input("Nova fruta: ")
frutas.append(novaFruta)

frutas.pop(0) #pop = remoção pela posição
#apagou o item da posição 0

frutas.remove("jaca") #remove = remoção pelo valor
#apagou o item com valor "jaca"

#=========MANEIRA-LEGAL-DE-USAR=========
filmes = ["Titanic"]

filmes.append("Lagoa Azul")

print("filmes")
print("1 - titanic")
print("2 - Lagoa azul")
filmeRemover = int(input("escolha a fruta a ser removida: "))
filmes.pop(filmeRemover - 1)
#=======================================

print(len(filmes))
#usando o len com lista ele não mostra a quantidade de caractere e sim a quantidade de itens

#para imprimir uma lista temos que usar for
for item in frutas:
    print(item)

#=====================================================
#posso guarda um valor de uma lista, para não perde apois mudar

marcas = ["nike", "Jordan", "Adidas"]

for i in marcas:
    print(i)

marcasAntigas = marcas #aqui eu salvei a lista marcas dentro da variavel marcasAntigas

marcas = ["roupas", "celulares","sapatos"] #aqui eu apaguei tudo que estava em marcas e coloquei novos valores

for i in marcas:
    print(i)

print(marcasAntigas) #aqui eu mostro as marcas que existiam antes da mudança

#========================================================



