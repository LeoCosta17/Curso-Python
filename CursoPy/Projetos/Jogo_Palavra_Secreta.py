import os

palavra_secreta =''
tentativa_usada = 0
caractere_digitado = ''
caractere_digitado_valido = len(caractere_digitado) < 1
letra_correta = caractere_digitado in palavra_secreta
acerto = ''

# Informe a palavra que o outro jogador deve descobrir
palavra_secreta = input('Informe a palavra secreta: ')
tentativas = len(palavra_secreta)

os.system('cls')

while tentativa_usada < tentativas:
    tentativa_usada += 1
    print(f'Tentativas: {tentativa_usada}/{tentativas}')
    caractere_digitado = input('Letra: ')

    if caractere_digitado_valido is not True:
        print('Digite apenas uma letra!')
        continue

    if letra_correta == True:
        acerto += caractere_digitado

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in acerto:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Parabéns! Você concluiu o jogo!')
        print(f'A palavra secreta era: {palavra_secreta}')
