#6 Realiza a leitura de 1 floatreferente ao salário do cidadão e apresenta o salário com reajuste de 10% da inflação.
valor = float(input('digite o valor do produto: '))

desconto10 = (valor * 10)/100
desconto10 = valor - desconto10

print('----------------------')
print('valor:', valor)
print('desconto de 10%:',desconto10)
print('----------------------')