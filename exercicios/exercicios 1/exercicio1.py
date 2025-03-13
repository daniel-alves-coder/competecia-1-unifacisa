#1 Realiza a leitura de 2 floatse imprime as seguintes operações: soma, subtração, multiplicação, divisão e resto da divisão

numero1 = float(input('digite o primeiro numero: '))
numero2 = float(input('digite o segundo numero: '))

soma = numero1 + numero2
subtração = numero1 - numero2
divisao = numero1 / numero2
multiplicacao = numero1 * numero2
resto = numero1 % numero2

print('soma:', soma)
print('subtração:', subtração)
print('multiplicação:', multiplicacao)
print('divisão:', divisao)
print('resto:', resto)