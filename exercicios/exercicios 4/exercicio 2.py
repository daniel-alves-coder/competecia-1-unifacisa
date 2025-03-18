'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a populaçãode
B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários
para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''

habitantesA = 80000
habitantesB =200000

crescimentoA = 3/100
crescimentoB = 1.5/100

ano = 0

while habitantesA < habitantesB:
    avancoA = (habitantesA * crescimentoA)
    avancoA = avancoA + habitantesA

    avancoB = (habitantesB * crescimentoB)
    avancoB = avancoB + habitantesB

    habitantesA = avancoA
    habitantesB = avancoB
    ano = ano + 1

print(habitantesA,"\n" + str(habitantesB) + "\n" + str(ano),"anos")


#resposta do chatGPT
'''
pop_A = 80000
pop_B = 200000
taxa_A = 1.03  # Crescimento de 3%
taxa_B = 1.015  # Crescimento de 1.5%
anos = 0

# Loop até que a população de A ultrapasse ou iguale a de B
while pop_A < pop_B:
    pop_A *= taxa_A
    pop_B *= taxa_B
    anos += 1

anos'''