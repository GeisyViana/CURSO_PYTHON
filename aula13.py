nome = 'Geisy'
altura = 1.60
peso = 43
imc = peso / (altura * altura)

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'Pesa {peso} quilos'
linha_3 = f'Seu IMC é: {imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)