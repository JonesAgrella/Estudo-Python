# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2 ?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5 ?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2 ? ',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


for pergunta in perguntas:
    print(f'Pergunta: {pergunta['Pergunta']}')

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i+1}) {opcao}')
    print()
...



