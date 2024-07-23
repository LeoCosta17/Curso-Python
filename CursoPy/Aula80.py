lista_nome = []
x = 0

while x < 5:
    nome = input('Insira um nome: ')
    lista_nome.append(nome)
    x += 1

print(lista_nome)

indice = int(input('Escolha um indice qualquer da lista:'))
print(lista_nome[indice])