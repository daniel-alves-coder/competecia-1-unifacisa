#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que
#ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa
#de R$ 4,00 por quilo excedente. 
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os
#dados do programa com as mensagens adequadas.

regulamento = 50
peso = float(input('Quantos kilos de peixe você pegou? '))
divida = False
multa = 0
 
if peso > regulamento:
    multa = peso - regulamento
    multa = multa * 4
    multa = round(multa,2)
    divida = True

b = '=' * 20

print(b)
print('estou com divida: {}'.format(divida))
print('a multa a ser paga é de: R${}'.format(multa))
print(b)



