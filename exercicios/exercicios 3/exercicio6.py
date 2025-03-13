"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades 
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

numero = int(input("Digite um numero de 1 a 999: "))
c = (numero // 100)
d = (numero %100) //10
u = (numero %10) //1

if numero >= 1 and numero < 1000:
    if c > 0: 
        centena = str(c)  + ' centena'
        if c > 1:
            centena = str(centena) + 's'
    else:
        centena = ""
    #dezena

    if d > 0: 
        dezena = str(d)  + ' dezena'
        if d > 1:
            dezena = str(dezena) + 's'
    else:
        dezena = ""
    #unidade

    if u > 0: 
        unidade = str(u)  + ' unidade'
        if u > 1:
            unidade = str(unidade) + 's'
            
    else:
        unidade = ""
    print(centena, dezena, unidade)


else:
    print("numero fora do padrão")

#tenho que terminar a atividade colocando "e" e as virgulas    

