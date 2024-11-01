primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'Primeiro Valor é maior "{primeiro_valor}" que Segundo valor "{segundo_valor}"!')

elif segundo_valor > primeiro_valor:
    print(f'Segundo valor é maior "{segundo_valor}" que Primeiro valor "{primeiro_valor}"!')

else:
    print('Os valores são iguais!')
