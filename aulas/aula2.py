        salario = 10050.12345
barra = '-' * 25
barra2 = '=' * 25
#print('O salario é %.2f' %salario)
#imprime o salario com duas casas decimais apenas


salario = round(salario,2)
#round converte salario para a quantidade de casas decimais, nesse caso 2

nota1, nota2 = 10, 5 #criar duas variaveis na mesma linha

print(nota1)
print(nota2)
print(barra)

restoDivisao = 5 % 2 #resto da divisão
potencia = 2**3 #potenciação
print('2 elevado a 3 é', potencia)
print(barra)

nome = 'Daniel'
sobrenome = 'Alves'

nomeCompleto = nome + ' ' + sobrenome #junta duas variaveis
print(nomeCompleto)
print(barra)

nomeTriplicado = nome * 3 #mostra o nome 3 vezes
print(nomeTriplicado)
print(barra)

tamanhoNome = len(nome) #len significa comprimento/extenção que mostra a quantidade de caracteres
print('O nome',nome,'tem',tamanhoNome,'letras')
print(barra)

nome = nome.upper() #upper significa maiusculo, transforma todas as letra em maiusculas
print(nome)
print(barra)

nome = nome.lower()#lower significa menusculo
print(nome)
print(barra)

nome = nome.capitalize() #com a primeira latra em maiusculo
print(nome)
print(barra, end=' ') # o end=" " diz que ao final do codigo ao inves de pular linha ele vai trocar por um espço


nome = nome.replace('D' or 'd','H') #replace significa subistituir, onde tiver "D" substituir por "H"
print(nome) #tambem dá pra substituir variaveis
print(barra)

print('O nome do cidadão é {} e o sobrenome é {}'.format(nome,sobrenome))
#outra forma de escrever o codigo e colocar as variaveis, coloca {} e depois aplica as variaveis na sequencia usando .format

