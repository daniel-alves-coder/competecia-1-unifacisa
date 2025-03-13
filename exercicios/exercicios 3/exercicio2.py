#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre
#pelo mais barato.

numero1 = int(input("digite o 1° numero: "))
numero2 = int(input("digite o 2° numero: "))
numero3 = int(input("digite o 3° numero: "))
maior = None

if numero1 < numero2 and numero1 < numero3:
    maior = 'produto 1'
elif  numero2 < numero1 and numero2 < numero3:
    maior = 'produto 2'
elif  numero3 < numero1 and numero3 < numero2:
    maior = 'produto 3'

print("o produto a ser comprado é o",maior)