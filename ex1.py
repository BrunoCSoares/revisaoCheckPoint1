'''
Escreva um programa em Python que solicite a altura e o sexo de uma pessoa. Em seguida, calcule seu peso ideal, utilizando as seguintes fórmulas:

- para homens: (72.7 * altura) – 58;

- para mulheres: (62.1 * altura) – 44.7.
'''

altura = float(input("Informe a altura: "))
sexo = input("Informe o sexo [m/f]: ")
peso_ideal = 0

match sexo:
    case 'm':
        peso_ideal = 72.7 * altura - 58
    case 'f':
        peso_ideal = 62.1 * altura - 44.7

print(f"O peso ideal é {peso_ideal}")