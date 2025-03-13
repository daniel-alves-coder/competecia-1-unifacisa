#10 Faça um programa que pede dois inteiro e armazene em duas variáveis. Em seguida, troque o valor das variáveis e
#exiba na tela

numero1 = int(input('primeiro numero: '))
numero2 = int(input('segundo numero: '))
numero3 = numero1
numero1 = numero2
numero2 = numero3

print('numero 1:',numero1)
print('numero 2', numero2)