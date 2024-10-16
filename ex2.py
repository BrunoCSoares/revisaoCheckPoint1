'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa em Python que irá calcular os reajustes.

Faça um programa que solicite ao usuário o salário de um colaborador e, em seguida, calcule o reajuste segundo o seguinte critério, baseado no salário atual:


- salários até R$ 280,00 (incluindo): aumento de 20%

- salários entre R$ 280,01 e R$ 700,00 : aumento de 15%

- salários entre R$ 700,01 e R$ 1500,00: aumento de 10%

- salários acima de R$ 1500,00: aumento de 5%


Após o aumento ser realizado, informe na tela o salário reajustado.
'''

salario_atual = float(input("Digite o salário do colaborador: R$ "))

if salario_atual <= 280:
    percentual = 20
elif salario_atual <= 700:
    percentual = 15
elif salario_atual <= 1500:
    percentual = 10
else:
    percentual = 5

aumento = salario_atual * (percentual / 100)
salario_reajustado = salario_atual + aumento

print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Salário após o reajuste: R$ {salario_reajustado:.2f}")
