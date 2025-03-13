#9 Faça um Programa que leia dois números inteiros e mostre o maior deles

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

if numero1 > numero2 :
    print('O maior é o', numero1)
elif numero1 == numero2:
    print('numeros iguais')
else: 
    print('O meior é', numero2)