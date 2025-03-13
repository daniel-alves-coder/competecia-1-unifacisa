#5 Realiza a leitura de 1 floatreferente ao valor de um produto e imprime o valor com descontos de 10%, 20% e 50%

valor = float(input('digite o valor do produto: '))

desconto20 = (valor * 0.2) #Abreviação da forma de caulcular porcentagem
desconto10 = (valor * 0.1)
desconto50 = (valor * 0.5)

desconto10 = valor - desconto10
desconto20 = valor - desconto20
desconto50 = valor - desconto50

print('----------------------')
print('valor:', valor)
print('desconto de 10%:',desconto10)
print('desconto de 20%:',desconto20)
print('desconto de 50%:',desconto50)
print('----------------------')