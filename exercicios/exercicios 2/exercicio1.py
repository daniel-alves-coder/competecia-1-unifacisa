#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#• Calcule e mostre o total do seu salário no referido mês.

horas = float(input('Quantas horas por dia você trabalha? '))
valorHora = float(input('Quanto você ganha por hora trabalhada? '))
extra = input('Você fez horas extras esse mês? ')
extra = extra.lower()

salario = horas * valorHora


if extra == 'sim':
    extra = float(input('Quantas horas extras você fez? '))
    salario = (horas + extra) * valorHora

salario = salario * 22
print('Salario do mês: {}'.format(salario))