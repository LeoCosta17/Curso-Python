import os

lista_compra = []
acao = ''

while True:
    os.system('cls')
    for indice, item in enumerate(lista_compra):
        print(f'{indice}-{item}')
    acao = input('[I]nserir, [D]eletar, [L]istar, [S]air').upper()
    if acao == 'I':
        lista_compra.append(input('Produto: '))
    elif acao == 'D':
        indice_lista = input('Item a ser apagado (indice): ')
        try:
            indice = int(indice_lista)
            del lista_compra[indice]
        except ValueError:
            print('Insita um número inteiro.')
        except IndexError:
            print('Indice inexistente.')
        except Exception:
            print('Erro desconhecido.')
    elif acao == 'L':
        for indice, item in enumerate(lista_compra):
            print(f'{indice}-{item}')
    elif acao == 'S':
        break