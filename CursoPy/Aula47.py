nome = input('Nome: ')
idade = input('Idade: ')

if nome != "" and idade != "":
    prim_letra_nome = nome[1]
    print(f'Primeira letra nome: {prim_letra_nome}')

    nome_inverso = nome[::-1]
    print(f'Nome ao contrário: {nome_inverso}')

    if " " in nome:
        print('Seu nome tem espaços')
    else:
        print('Seu nome não tem espaços')

    print(f'Quantidade letras: {len(nome)}')

    print(f'Última letra: {nome[len(nome)-1]}')