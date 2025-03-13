idade = int(input('qual a sua idade? '))# tranforma a string que veio de um input em inteiro

nome = 'Daniel'
salario  = 5000.502535

salario = round(salario,2) #so apresenta 2 casas decimais

status = None #None significa nenhum valor

print(nome,' tem ',idade,' anos e ganha ',salario,' de salario')

print(type(status))# mostra o tipo da variavel que no caso é boolean

if idade >=18:
    status = True
else:
    status = False

print(nome,'é maior de idade?',status)
print(type(status))


