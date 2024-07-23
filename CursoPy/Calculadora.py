while True:
    
    try:
        n1 = float(input('Insert: '))
        n2 = float(input('Insert: '))
    except Exception as error:
        print(f'Número inválido. ERRO: {error}')
        break

    sair = input('Finalizar? [S]im').lower().startswith('s')

    if sair is True:
        break

    operacao = input('Operação:[+ - * / **] ')
    
    resultado = 0

    if operacao == '+':
        resultado = n1 + n2
    elif operacao == '-':
        resultado = n1 - n2
    elif operacao == '*':
        resultado = n1 * n2
    elif operacao == '/':
        resultado = n1 / n2
    elif operacao == '**':
        resultado = n1 ** n2
    else:
        print('Operação inválida!')
        break
    
    print(f'Resultado: {resultado}')