'''
Faça um programa em Python que solicite ao usuário o valor de n e que mostre os n termos da Série a seguir:

S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

Nesse caso, utilize a estrutura de repetição “for”.
'''

n = int(input("Digite o valor de n: "))
soma = 0
m = 1

for i in range(1, n + 1):
    soma += i / m
    m += 2

print(f"Soma da série: {soma:.2f}")
