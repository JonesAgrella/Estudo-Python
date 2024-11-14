indice = 0
nome = 'jones'
novo_nome = ''

while  indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1 

novo_nome += '*'
print(novo_nome)
