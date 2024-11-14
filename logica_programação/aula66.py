"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)

#CPF: 746.824.890-70

#Primero Digito
regressivo_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
lista_soma_digitos_1 = []

cpf = input('CPF: ')
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')

digitos_1 = cpf[:9]
for i, digito in enumerate(digitos_1):
    soma_1 = int(digito) * regressivo_1[i]
    lista_soma_digitos_1.append(soma_1)

resultado_digitos_1 = (sum(lista_soma_digitos_1) * 10 ) % 11

resultado_digitos_1 if resultado_digitos_1 <= 9 else 0


#Segundo Digito
regressivo_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
lista_soma_digitos_2 = []

digitos_2 = cpf[:10]
for i, digito in enumerate(digitos_2):
    soma_2 = int(digito) * regressivo_2[i]
    lista_soma_digitos_2.append(soma_2)

resultado_digitos_2 = (sum(lista_soma_digitos_2) * 10) % 11

resultado_digitos_2 if resultado_digitos_2 <= 9 else 0

cpf_gerado = f'{cpf[:9]}{resultado_digitos_1}{resultado_digitos_2}'

if cpf == cpf_gerado:
    print(f'CPF: {cpf} é Válido')
else: 
    print(f'CPF: {cpf} é Inválido')
