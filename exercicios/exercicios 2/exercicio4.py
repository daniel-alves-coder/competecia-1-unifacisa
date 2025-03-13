#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu
#salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um
#programa que nos dê:
#• salário bruto.
#• quanto pagou ao INSS.
#• quanto pagou ao sindicato.
#• o salário líquido.
#• calcule os descontos e o salário líquido, conforme a tabela à direita.

b = '=' * 25
horas = float(input('Quantas horas por dia você trabalha? '))
valorHora = float(input('Quanto você ganha por hora trabalhada? '))
extra = input('Você fez horas extras esse mês? ')
extra = extra.lower()

salario = horas * valorHora


if extra == 'sim':
    extra = float(input('Quantas horas extras você fez? '))
    salario = (horas + extra) * valorHora

salarioBruto = salario * 22

impostoDeRenda = (salarioBruto * 11)/100

sindicato = (salarioBruto *5)/100

inss = (salarioBruto * 8)/100

salarioLiquido = salarioBruto - (impostoDeRenda + inss + sindicato)

print(b)
print('Salario Bruto: {}'.format(salarioBruto))
print('INSS: R$',inss)
print('sindicato: R$',sindicato)
print('Imposto de renda: R$',impostoDeRenda)
print('salario liquido: R$', salarioLiquido)
print(b)