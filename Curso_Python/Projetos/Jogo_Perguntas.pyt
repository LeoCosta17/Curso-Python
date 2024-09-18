perguntas = [
    {
        'Pergunta' : 'Quem é o maior país da América Latina?',
        'Opções' : ['Chile', 'Brazil', 'Paraguai', 'Colombia'],
        'Resposta' : '1'
    },

    {
        'Pergunta' : 'Qual desses animais é um réptil?',
        'Opções' : ['Tubarão', 'Avestruz', 'Crocodilo', 'Cachorro'],
        'Resposta' : '2'
    },

    {
        'Pergunta' : 'Qual é a maior cidade?',
        'Opções' : ['Buenos Aires', 'Piracicaba', 'Montevidéu', 'São Paulo'],
        'Resposta' : '3'
    }
]

contador_acertos = 0
contador_erros = 0

for pergunta in perguntas:
    print(f'Pergunta: {pergunta['Pergunta']}')

    print()

    for indice, opcao in enumerate(pergunta['Opções']):
        print(f'{indice} - {opcao}')

    resposta = input(f'Resposta: ')
    try:
        resposta = int(resposta)
        if resposta == pergunta['Resposta']:
            contador_acertos += 1
            print('Você acertou!')
        else:
            contador_erros += 1
            print('Você errou!')
    except ValueError as error:
        print(f'Informe apenas numerais! {error}')

    print()

resultado_final = f'Acertos: {contador_acertos}\nErros: {contador_erros}'

print('Resultado final:')
print(resultado_final)