b = "="*20
#usando o range
'''
range() gera uma LISTA de numeros
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
