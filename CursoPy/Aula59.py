resposta = input('Deseja iniciai o loop? ')

while resposta == 'S':
    print('Executando pela novamente')
    resposta = input('Deseja continuar? ')
    if resposta != 'S':
        break
    
print('Loop finalizado')