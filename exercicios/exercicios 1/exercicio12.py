#12 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e
#calcule a sua média. A atribuição de conceitos deve obedecer à tabela abaixo.
#Média Conceito
#Entre 9 e 10 - A
#Entre 7.5 e 9 - B
#Entre 6 e 7.5 - C
#Entre 4 e 6 - D
#Entre 0 e 4 - E

nota1 = float(input('Qual a sua primeira nota? '))
nota2 = float(input('Qual a sua primeira nota? '))
media = (nota1 + nota2)/2

if media >= 0 and media <= 4:
    classificacao = 'E'
elif media > 4 and media <= 6:
    classificacao = 'D'
elif media > 6 and media <= 7.5:
    classificacao = 'C'
elif media > 7.5 and media < 9:
    classificacao = 'B'
elif media >= 9 and media <=10:
    classificacao = 'A'
else: classificacao = 'improvavel'

print('===================')
print('Nome: Daniel')
print('Media:',classificacao)
print('===================')