#• Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#• o produto do dobro do primeiro com metade do segundo .
#• a soma do triplo do primeiro com o terceiro.
#• o terceiro elevado ao cubo.


n1 = int(input('digite o prieiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = float(input('digite o terceiro numero: '))

prod = (n2/2)*(n1*2)
soma = (3 * n1) + n3
eleva = n3 ** 3


print(prod)
print(soma)
print(eleva)