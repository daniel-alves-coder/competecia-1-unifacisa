letras = ["m","a","r","a","c","u","j","a"]

barras = ["-","-","-","-","-","-","-","-"]

erros = 0

while True:
    digito = input("Digite a letra: ")

    if digito in letras:
        posicoes = []

        for i, letra in enumerate(letras):
            if letra == digito:
                posicoes.append(i)

        for index in posicoes:
            barras[index] = digito
    else:
        erros = erros + 1

    print(f"erros: {erros}/{len(letras)}")

    for letra in barras:
        print(letra, end = " ")
    print()

    if letras == barras:
        print("Ganhouuuu")
        break
    elif erros == len(letras):
        print("perdeu")
        break

print("fim do jogo")