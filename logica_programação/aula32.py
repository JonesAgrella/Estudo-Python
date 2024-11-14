"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

#code 01
# numero = input('Digite um número: ')


# try:
#     numero_int = int(numero)
#     par_impar = numero_int % 2
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'
    
#     print(f'Número: {numero_int} é {par_impar_texto}')

# except: 
#     print(f'Número: {numero} não é inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# # code 02
# hora = int(input('Digite as horas: '))

# if 23 >= hora >= 18:
#     print('Boa Noite')
# elif 17 >= hora >= 12:
#     print('Boa Tarde')
# elif 11 >= hora:
#     print('Bom Dia')
# else:
#     print('Hora Inválida')



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# code 03
nome = str(input("Digite seu nome: "))

if len(nome) <= 4:
    print('Nome: pequeno')
elif len(nome) <= 6:
    print('Nome: médio')
else:
    print('Nome: grande')

