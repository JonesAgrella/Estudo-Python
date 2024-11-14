"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista= []
lista_apagados = []

while True:
    opção = str(input('Escolha uma opção\n[i]nserir [a]pagar [l]istar [s]air\nOpção: '))
    opção = opção.lower()
    limpar = os.system('cls')

    if opção == 'i':
        item = str(input('Escreva o item na lista: '))
        if len(item) > 2:
            item = item.capitalize()
            lista.append(item)
            limpar
        else:
            print('Item deve conter mais de 2 caracteres, Tente Novamente')
            continue

    elif opção == 'a':
        if lista:
            apagar = input('Escreva o número do item da lista para apagar: ')
            try:
                apagar = int(apagar)
                apagar -= 1
                remover_lista = lista.pop(apagar)
                limpar   
            except:
                print('Digite o número do item para pagar')
                for i, item in enumerate(lista):
                    print(f'N:{i + 1} - {item}')
                    continue

    elif opção == 'l':
        print('Lista:')
        for i, item in enumerate(lista):
            print(f'N:{i + 1} - {item}')
    
    elif opção == 's':
        print('Lista:')
        for i, item in enumerate(lista):
            print(f'N:{i + 1} - {item}')
        limpar
        break

    else:
        print('Opção não conpátivel, Tente Novamente!')
        continue
    
    