""" Calculadora com While"""

while True:
    num_1_float = input('Digite um número: ')
    num_2_float = input('Digite outro número: ')
    operador = input('Digite o operador(+, -, *, /): ')

#______________________________________________________________
# Tratamento dos dados recebidos
    numeros_validos = None

    try:
        num_1_float = float(num_1_float)
        num_2_float = float(num_2_float)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números são inválidos!')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue
#______________________________________________________________
# Cálculos

    print('Resultado:')
    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float) 
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
    else:
        print('Nunca deveria acontecer')

#______________________________________________________________
# Break
    sair = input('Quer sair? [s]im ou [n]ão: ').lower().startswith('s')
    
    if sair:
        break