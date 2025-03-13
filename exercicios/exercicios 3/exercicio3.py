#Faça um Programa que leia três números e mostre-os em ordem decrescente.


numero1 = int(input("digite o 1° numero: "))
numero2 = int(input("digite o 2° numero: "))
numero3 = int(input("digite o 3° numero: "))
maior = None
meio = None
menor = None

if (numero1 < numero2 and numero1 < numero3) and (numero2 < numero3):
    maior = numero3
    meio = numero2
    menor = numero1
    print('sequencia 1')

elif  (numero2 < numero1 and numero2 < numero3) and (numero1 < numero3):
    maior = numero3
    meio = numero1
    menor = numero2
    print('sequencia 2')
elif (numero3 < numero1 and numero3 < numero2) and (numero1 < numero2):
    maior = numero2
    meio = numero1
    menor = numero3
    print('sequencia 3')

print(maior)
print(meio)
print(menor)