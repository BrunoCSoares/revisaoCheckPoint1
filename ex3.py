'''
Quando ações são vendidas ou compradas por meio de um corretor, a comissão do corretor é muitas vezes calculada usando uma escala que depende do valor das ações negociadas. Escreva um programa em Python que calcule e exiba o valor da comissão a partir do valor da transação informado pelo usuário, sabendo-se que o corretor cobra os valores indicados abaixo e que a comissão mínima é de R$ 39,00:


● Até R$ 2.500,00, comissão de R$30 + 1,7%

● R$2.500,01 até R$6.250,00, comissão de R$56 + 0,66%

● R$6.250,01 até R$20.000,00, comissão de R$76 + 0,34%

● R$20.000,01 até R$50.000,00, comissão de R$100 + 0,22%

● R$50.000,01 até R$500.000,00, comissão de R$155 + 0,11%

● Mais que R$ 500.000,00, comissão de R$255 + 0,09%
'''

valor_transacao = float(input("Digite o valor da transação: R$ "))

comissao_minima = 39.00

if valor_transacao <= 2500:
    comissao = 30 + (valor_transacao * 0.017)
elif valor_transacao <= 6250:
    comissao = 56 + (valor_transacao * 0.0066)
elif valor_transacao <= 20000:
    comissao = 76 + (valor_transacao * 0.0034)
elif valor_transacao <= 50000:
    comissao = 100 + (valor_transacao * 0.0022)
elif valor_transacao <= 500000:
    comissao = 155 + (valor_transacao * 0.0011)
else:
    comissao = 255 + (valor_transacao * 0.0009)

if comissao < comissao_minima:
    comissao = comissao_minima

print(f"Comissão: R$ {comissao:.2f}")
