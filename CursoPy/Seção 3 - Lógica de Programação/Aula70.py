frase = 'Abacaxi'

i = 0
qtd_apareceu_mais = 0
letra_mais_apareceu = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_letra = frase.count(letra_atual)

    if qtd_apareceu_mais < qtd_letra:
        qtd_apareceu_mais = qtd_letra
        letra_mais_apareceu = letra_atual

    i+=1

print (f'Letra mais repetida: {letra_mais_apareceu} Qtd: {qtd_apareceu_mais}')