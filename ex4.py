'''
Escreva um programa em Python para ler 10 valores e escrever quantos desses valores lidos estão no intervalo [10,20] (incluindo os valores 10 e 20 no intervalo) e quantos deles estão fora deste intervalo. Nesse caso, utilize a estrutura de repetição “for”.
'''

dentro_intervalo = 0
fora_intervalo = 0

for _ in range(10):
    valor = int(input("Digite um valor: "))
    if 10 <= valor <= 20:
        dentro_intervalo += 1
    else:
        fora_intervalo += 1

print(f"Valores no intervalo [10,20]: {dentro_intervalo}")
print(f"Valores fora do intervalo: {fora_intervalo}")
