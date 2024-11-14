"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Jones')
#__________________________________

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])

#or

# for i in enumerate(lista):
#     print(i)
