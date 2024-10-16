'''
Numa eleição existem três candidatos. Faça um programa em Python que solicite ao usuário o número total de eleitores. Em seguida, peça para cada eleitor votar e ao final mostre o número de votos de cada candidato. Nesse caso, utilize a estrutura de repetição “for”.
'''

total_eleitores = int(input("Digite o número total de eleitores: "))

votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

for i in range(total_eleitores):
    voto = int(input("Vote no candidato (1, 2 ou 3): "))

    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    else:
        print("Voto inválido!")

print(f"Votos do candidato 1: {votos_candidato1}")
print(f"Votos do candidato 2: {votos_candidato2}")
print(f"Votos do candidato 3: {votos_candidato3}")
