'''
combinando AND e OR
NOT
!=
if aninhado
'''

b = '=' * 30

idade = 32
salario = 2100
print(b)
if (idade >= 28 and idade < 40) or salario >= 20000: #combinando AND e OR em uma condição
    print('Voce tem a cesso ao banco')
else: 
    print('Voce não pode usar esse banco')
print(b)

if not salario >= 20000: # o NOT inverte a condição, agora a mensagem vai aparecer se o salario for menor que 20.000
    print('seu salario não é maior ou igual a 20.000') 
print(b)
if idade != 20: # esse é o sinal de diferente, entao fica: se idade for diferente de 20
    print('voce não tem 20 anos')


#colocando um if dentro do outro
print(b)
numero = -6

if numero >= 0:
    if numero == 0:
        print('zero')
    else: 
        print('positivo')
else: 
    print('negativo')

print(b)

#==============================================