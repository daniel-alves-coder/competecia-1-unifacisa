#Faça um Programa que leia três números e mostre o maior deles.

numero1 = int(input("digite o 1° numero: "))
numero2 = int(input("digite o 2° numero: "))
numero3 = int(input("digite o 3° numero: "))
maior = None

if numero1 > numero2 and numero1 > numero3:
    maior = numero1
elif  numero2 > numero1 and numero2 > numero3:
    maior = numero2
elif  numero3 > numero1 and numero3 > numero2:
    maior = numero3

print('O maior é o numero',maior)