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
#======================================

#usando o range
'''
range(n) na qual gera números de 0 até n-1
Por exemplo, range(3) gera 0,1 e 2

• range(a,n) na qual gera números de a até n-1
• Por exemplo, range(1,3) gera 1 e 2

• range(a,n,s) na qual gera números de a até n-1, pulando de s em s
• Por exemplo, range(0,5,2) em teoria geraria
0,1,2,3,4 . Entretanto, o último parâmetro
(s) que tem o valor 2 significa que ele pula
de 2 em 2. Como assim? No 0, ele pula
diretamente para 2 e do 2 exatamente para
o 4, de modo que os 1 e 3 são
desconsiderados.
'''

lista = range(3) #range gera uma lista de numeros
for i in lista: #for abre/apresenta/mostra todos os numeros da lista
    print('Numero: ',i)


print(b)

lista = range(2,6) #de 2 a 6
for i in lista:
    print('Numero: ',i)

print(b)
lista = range(1,7,2) #de 1 a 7 pulando de 2 em 2
for i in lista:
    print('Numero: ',i)
print(b)

#==============================================