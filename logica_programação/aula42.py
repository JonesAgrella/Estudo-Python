frase = 'A frase digitada será essa aqui no modo qwert'.lower()

letra_maior_quantidade_num = 0
letra_maior_quantidade_str = ''
i = 0 

while i < len(frase):
    letra_atual = frase[i]
    qtde_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if letra_maior_quantidade_num < qtde_atual:
        letra_maior_quantidade_num = qtde_atual
        letra_maior_quantidade_str = letra_atual

    i += 1

print(f'Letras que mais apareceu: "{letra_maior_quantidade_str}" {letra_maior_quantidade_num} vezes')
