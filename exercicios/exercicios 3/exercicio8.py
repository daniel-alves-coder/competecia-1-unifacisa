info = {
    "nome" : "",
    "habilidade" : 0,
    "sorte" : 0,
    "vida" : 0
}
print(info["nome"])
def play():
    info["nome"] = input("Digite o nome do seu personagem: ")
    info["habilidade"] = int(input("Digite a habilidade: "))
    info["vida"] = int(input("Digite a vida: "))
    info["sorte"] = int(input("Digite a sorte: "))

def combate():
    vida = info["vida"]
    vida = vida - 2
    info["vida"] = vida

def elixir():
    vida = info["vida"]
    vida = vida + 1
    info["vida"] = vida

play()
combateSorN = input("Quer combater? [s/n]")

if combateSorN in "Ss":
    combate()
else:
    pass

print(info["vida"])

