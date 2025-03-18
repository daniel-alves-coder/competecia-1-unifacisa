'''
Faça um programa que leia e valide as seguintes informações:
• Nome: maior que 3 caracteres;
• Idade: entre 0 e 150;
• Salário: maior que zero;
• Sexo: 'f' ou 'm';
• Estado Civil: 's', 'c', 'v', 'd’;
'''

sex = ["masculino","feminino"]
estado = ["solteiro","casado","vilvo","divorciado"]

#Nome
nome = input("Digite seu nome: ")
if len(nome) < 4:
    while len(nome) <4:
        print("Nome invalido - tente um nome com mais de 4 caracteres")
        nome = input("Digite seu nome: ")
#Idade
idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 150:
    pass
else:
    while idade <= 0 or idade >= 150:
        print("idade invalida")
        idade = int(input("Digite sua idade: "))

#Salario
salario = int(input("Digite seu salario: "))
if salario >0:
    pass
else:
    while salario <=0:
        print("Não aceitamos salarios zerados")
        salario = int(input("Digite seu salario: "))

#Sexo
for i in range(len(sex)):
    print(i + 1, "-", sex[i])
sexo = int(input("Digite o codigo do seu sexo: "))
sexo = sexo - 1
if sexo in range(len(sex)):
    pass
else:
    while sexo not in range(len(sex)):
        for i in range(len(sex)):
            print(i + 1, "-", sex[i])
        sexo = int(input("Digite o codigo do seu sexo: "))
        sexo = sexo - 1

#Estado Civil
for i in range(len(estado)):
    print(i + 1,"-",estado[i])
estadoCivil = int(input("Digite o codigo do seu estado civil: "))
estadoCivil = estadoCivil - 1

if estadoCivil in range(len(estado)):
    pass
else:
    while estadoCivil not in range(len(estado)):
        for i in range(len(estado)):
            print(i + 1, "-", estado[i])
        estadoCivil = int(input("Digite o codigo do seu Estado Civil: "))
        estadoCivil = estadoCivil - 1

#SAIDA
print("nome:",nome,"\nidade:",idade,"\nsalario:",salario,"\nsexo:",sex[sexo],"\nestado civil:",estado[estadoCivil])